#Lesson Mocking                     date 18/03/2025

#Exercise n2 Mocking lidar readings

import pytest

from unittest.mock import patch

from lidar_readings import get_lidar_readings


def get_obstacle_data():
    """Refer to previous example docstring"""
    readings = get_lidar_readings()
    if readings is not None:
        angles, distances = parse_lidar_data(readings)
        return {'angles': angles, 'distances': distances}
    else:
        return None


def parse_lidar_data(data) -> tuple:
    angles = [d[0] for d in data]
    distances = [d[1] for d in data]
    return angles, distances


def test_get_obstacle_data():
    mock_data = [(11, 100), (12, 50), (123, 150)]
    with patch("parse_lidar_readings.get_lidar_readings", return_value=mock_data) as mock_get_lidar:
        result = get_obstacle_data()

        # Verify that the function was called
        mock_get_lidar.assert_called_once()

        # Expected output after parsing
        expected_result = {"angles": [11, 12, 123], "distances": [100, 50, 150]}

        assert result == expected_result


def test_get_obstacle_data_no_readings():
    """Test that get_obstacle_data returns None when get_lidar_readings returns None."""
    with patch("parse_lidar_readings.get_lidar_readings", return_value=None) as mock_get_lidar:
        result = get_obstacle_data()

        # Verify that the function was called
        mock_get_lidar.assert_called_once()

        # Expect None if no readings are available
        assert result is None