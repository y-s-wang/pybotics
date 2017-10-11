import numpy as np

from pybotics.geometry import wrap_2_pi, euler_zyx_2_matrix, matrix_2_euler_zyx

np.set_printoptions(suppress=True)

EULER_ZYX_VECTOR = np.array([100, 200, 300, np.deg2rad(-30), np.deg2rad(50), np.deg2rad(90)])
TRANSFORM = np.array([
    [0, -0.642788, 0.766044, 100],
    [0.866025, 0.383022, 0.321394, 200],
    [-0.5, 0.663414, 0.556670, 300],
    [0, 0, 0, 1]
])


def test_euler_zyx_2_matrix():
    actual = euler_zyx_2_matrix(EULER_ZYX_VECTOR)
    np.testing.assert_allclose(actual=actual, desired=TRANSFORM, atol=1e-6)


def test_matrix_2_euler_zyx():
    actual = matrix_2_euler_zyx(TRANSFORM)
    np.testing.assert_allclose(actual=actual, desired=EULER_ZYX_VECTOR, atol=1e-6)


def test_wrap_2_pi():
    angles = np.array([
        [0, 0],
        [-np.pi, -np.pi],
        [np.pi, -np.pi],
        [2 * np.pi, 0],
        [-2 * np.pi, 0]
    ])

    test_angles = angles[:, 0]
    expected_angles = angles[:, 1]

    actual_angles = np.array(map(wrap_2_pi, test_angles))
    assert len(test_angles) == len(expected_angles)
    assert len(actual_angles) == len(expected_angles)
    np.testing.assert_allclose(actual_angles, expected_angles)

    # test single elements
    for i, _ in enumerate(expected_angles):
        actual_angle = wrap_2_pi(test_angles[i])
        np.testing.assert_allclose(actual_angle, expected_angles[i])
