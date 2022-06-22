

from http import HTTPStatus

from faker import Faker

from .http import HttpStatus

sut = HttpStatus()
faker = Faker()


def test_should_return_correct_ok_200():
    body = faker.name()
    result = sut.ok_200(body)
    assert result.status_code == 200
    assert result.body == body


def test_should_return_correct_created_201():
    body = faker.name()
    result = sut.created_201(body)
    assert result.status_code == 201
    assert result.body == body


def test_should_return_correct_error_400():
    error = faker.sentence()
    result = sut.bad_request_400(error)
    assert result.status_code == 400
    assert result.body["error"] == error
    result = sut.bad_request_400()
    assert result.status_code == 400
    assert result.body["error"] == "Bad Request"


def test_should_return_correct_unauthorized_401():
    error = faker.sentence()
    result = sut.unauthorized_401(error)
    assert result.status_code == 401
    assert result.body["error"] == error
    result = sut.unauthorized_401()
    assert result.status_code == 401
    assert result.body["error"] == "Unauthorized"


def test_should_return_correct_forbidden_403():
    error = faker.sentence()
    result = sut.forbidden_403(error)
    assert result.status_code == 403
    assert result.body["error"] == error
    result = sut.forbidden_403()
    assert result.status_code == 403
    assert result.body["error"] == "Forbidden"


def test_should_return_correct_not_found_404():
    error = faker.sentence()
    result = sut.not_found_404(error)
    assert result.status_code == 404
    assert result.body["error"] == error
    result = sut.not_found_404()
    assert result.status_code == 404
    assert result.body["error"] == "Not Found"


def test_should_return_correct_conflict_409():
    error = faker.sentence()
    result = sut.conflict_409(error)
    assert result.status_code == 409
    assert result.body["error"] == error
    result = sut.conflict_409()
    assert result.status_code == 409
    assert result.body["error"] == "Conflict"


def test_should_return_correct_unprocessable_entity_422():
    error = faker.sentence()
    result = sut.unprocessable_entity_422(error)
    assert result.status_code == 422
    assert result.body["error"] == error
    result = sut.unprocessable_entity_422()
    assert result.status_code == 422
    assert result.body["error"] == "Unprocessable Entity"


def test_should_return_correct_internal_server_error_500():
    error = faker.sentence()
    result = sut.internal_server_error_500(error)
    assert result.status_code == 500
    assert result.body["error"] == error
    result = sut.internal_server_error_500()
    assert result.status_code == 500
    assert result.body["error"] == "Internal Server Error"


def test_should_return_correct_error_406():
    faker_message = faker.sentence()
    result = sut.not_acceptable_406(faker_message)
    assert result.status_code == 406
    assert result.body["error"] == faker_message

    result = sut.not_acceptable_406()
    assert result.status_code == 406
    assert result.body["error"] == HTTPStatus.NOT_ACCEPTABLE.phrase

    result = sut.not_acceptable_406(faker_message)
    assert result.status_code == 406
    assert result.body["error"] == faker_message