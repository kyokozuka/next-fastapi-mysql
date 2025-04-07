import pytest
from unittest.mock import MagicMock
from src.domain.sample.model.new_sample_model import NewSampleModel

from src.domain.sample.model.sample_model import SampleModel
from src.domain.sample.model.sample_id import SampleID
from src.infrastructure.db.model.sample import SampleDBModel
from src.domain.sample.model.sample_message import SampleMessage
from src.domain.sample.model.sample_name import SampleName
from src.infrastructure.repository.sample_repository import SampleRepositpry
from fastapi import HTTPException


class TestSampleRepositpry:

    def test_sucess_new_sample(self):
        # Arrange
        mock_sample = NewSampleModel(
            name=SampleName(value="Test Sample"),
            message=SampleMessage(value="This is a test sample"),
        )
        return_sample = SampleDBModel(
            name="Test Sample",
            message="This is a test sample",
        )
        mock_session = MagicMock()
        mock_session.add.return_value = return_sample
        mock_session.flush.return_value = None

        # Act
        repository = SampleRepositpry(mock_session)
        result = repository.new_sample(mock_sample)

        # Assert
        assert result.name.value == return_sample.name
        assert result.message.value == return_sample.message

    def test_exception_new_sample(self):
        # Arrange
        mock_sample = NewSampleModel(
            name=SampleName(value="Test Sample"),
            message=SampleMessage(value="This is a test sample"),
        )
        mock_session = MagicMock()
        mock_session.add.side_effect = Exception("Database error")

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(Exception) as excinfo:
            repository.new_sample(mock_sample)

        # Assert
        assert str(excinfo.value) == "Database error"

    def test_success_list_sample(self):
        # Arrange
        mock_sample = SampleDBModel(
            name="Test Sample",
            message="This is a test sample",
        )
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.all.return_value = [
            mock_sample
        ]

        # Act
        repository = SampleRepositpry(mock_session)
        result = repository.list_sample()

        # Assert
        assert len(result) == 1
        assert result[0].name.value == mock_sample.name
        assert result[0].message.value == mock_sample.message

    def test_http_exception_list_sample(self):
        # Arrange
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value = None

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(HTTPException) as excinfo:
            repository.list_sample()

        # Assert
        assert excinfo.value.status_code == 404
        assert excinfo.value.detail == "Sample not found"

    def test_exception_list_sample(self):
        # Arrange
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.all.side_effect = Exception(
            "Database error"
        )

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(Exception) as excinfo:
            repository.list_sample()

        # Assert
        assert str(excinfo.value) == "Database error"

    def test_success_get_sample(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_sample = SampleDBModel(
            name="Test Sample",
            message="This is a test sample",
        )
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.return_value = (
            mock_sample
        )

        # Act
        repository = SampleRepositpry(mock_session)
        result = repository.get_sample(sample_id)

        # Assert
        assert result.name.value == mock_sample.name
        assert result.message.value == mock_sample.message

    def test_http_exception_get_sample(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.return_value = None

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(HTTPException) as excinfo:
            repository.get_sample(sample_id)

        # Assert
        assert excinfo.value.status_code == 404
        assert excinfo.value.detail == "Sample not found"

    def test_exception_get_sample(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.side_effect = (
            Exception("Database error")
        )

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(Exception) as excinfo:
            repository.get_sample(sample_id)

        # Assert
        assert str(excinfo.value) == "Database error"

    def test_success_update(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_sample = SampleModel(
            id=sample_id,
            name=SampleName(value="Updated Sample"),
            message=SampleMessage(value="This is an updated test sample"),
        )
        return_sample = SampleDBModel(
            name="Updated Sample",
            message="This is an updated test sample",
        )
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.return_value = (
            return_sample
        )

        # Act
        repository = SampleRepositpry(mock_session)
        result = repository.update(mock_sample)

        # Assert
        assert result.name.value == return_sample.name
        assert result.message.value == return_sample.message

    def test_http_exception_update(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_sample = SampleModel(
            id=sample_id,
            name=SampleName(value="Updated Sample"),
            message=SampleMessage(value="This is an updated test sample"),
        )
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.return_value = None

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(HTTPException) as excinfo:
            repository.update(mock_sample)

        # Assert
        assert excinfo.value.status_code == 404
        assert excinfo.value.detail == "Sample not found"

    def test_exception_update(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_sample = SampleModel(
            id=sample_id,
            name=SampleName(value="Updated Sample"),
            message=SampleMessage(value="This is an updated test sample"),
        )
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.side_effect = (
            Exception("Database error")
        )

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(Exception) as excinfo:
            repository.update(mock_sample)

        # Assert
        assert str(excinfo.value) == "Database error"

    def test_success_delete(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_sample = SampleDBModel(
            name="Test Sample",
            message="This is a test sample",
        )
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.return_value = (
            mock_sample
        )

        # Act
        repository = SampleRepositpry(mock_session)
        result = repository.delete(sample_id)

        # Assert
        assert result is None

    def test_http_exception_delete(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.return_value = None

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(HTTPException) as excinfo:
            repository.delete(sample_id)

        # Assert
        assert excinfo.value.status_code == 404
        assert excinfo.value.detail == "Sample not found"

    def test_exception_delete(self):
        # Arrange
        sample_id = SampleID(value=1)
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.first.side_effect = (
            Exception("Database error")
        )

        # Act
        repository = SampleRepositpry(mock_session)
        with pytest.raises(Exception) as excinfo:
            repository.delete(sample_id)

        # Assert
        assert str(excinfo.value) == "Database error"
