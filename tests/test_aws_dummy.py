import mock
import pytest
from deployer import aws_dummy as aws


def test_init_adapter_is_callable():
    aws.init_adapter({})
    assert True


def test_get_latest_images_from_ecr_registry():
    images = aws.get_latest_images_from_ecr_registry({}, 'fake_registry_id')

    assert images == {
        'fake_repo_name': (3, ),
        'second_image': (23, )
    }


def test_get_current_images_on_ecs():
    images = aws.get_current_images_on_ecs({}, 'fake_region')

    assert images == {
        'first_image': (23, 'service_name'),
        'second_image': (23, 'service_name')
    }
