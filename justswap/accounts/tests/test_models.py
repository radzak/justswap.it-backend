# -*- coding: utf-8 -*-

import pytest
from django.core.exceptions import ValidationError

from justswap.accounts.models import User, username_validator


class TestUserNameValidator:
    """Test suite for username validation."""

    def test_valid_username(self):
        """This test ensures that alphanumeric characters are valid for a username."""
        username_validator("abcde234")

    def test_long_username(self):
        """This test ensures that a username of 15 characters is valid."""
        username_validator("a" * 15)

    def test_short_username(self):
        """This test ensures that a username of 3 characters is valid."""
        username_validator("b" * 3)

    def test_too_long_username(self):
        """This test ensures that a username can't be too long."""
        with pytest.raises(ValidationError):
            username_validator("c" * 16)

    def test_too_short_username(self):
        """This test ensures that a username can't be too short."""
        with pytest.raises(ValidationError):
            username_validator("a")

    def test_not_alphanumeric_username(self):
        """This test ensures that non-alphanumeric characters are forbidden."""
        with pytest.raises(ValidationError):
            username_validator("hdfg#@$*&((@")


class TestUserModel:
    """Test suite for custom User model."""

    @pytest.mark.django_db
    def test_save_model(self, normal_user):
        """This test ensures that saving the user instance works."""
        normal_user.save()

    def test_short_name(self, normal_user):
        """This test ensures that short name is correctly evaluated."""
        normal_user.first_name = None
        assert normal_user.get_short_name() == normal_user.username
        normal_user.first_name = "someone"
        assert normal_user.get_short_name() == normal_user.first_name

    def test_full_name(self, normal_user):
        """This test ensures that full name is correctly evaluated."""
        normal_user.first_name = None
        assert normal_user.get_full_name() == normal_user.username
        normal_user.first_name = "someone"
        normal_user.last_name = "someone"
        assert normal_user.get_full_name() == "someone someone"


@pytest.mark.django_db
class TestUserManager:
    """Test suite for custom User manager."""

    def test_create_user(self):
        """This test ensures successful creation and email lookup of a regular user."""
        email = "something@c.c"
        user = User.objects.create_user(username="something", email=email)
        assert user == User.objects.get(email=email)

    def test_create_superuser(self):
        """This test ensures successful creation and email lookup of a super user."""
        email = "something@c.c"
        user = User.objects.create_superuser(  # noqa: S106
            username="something", email=email, password="test"
        )
        assert user == User.objects.get(email=email)
        assert user.is_superuser
