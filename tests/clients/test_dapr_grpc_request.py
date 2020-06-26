# -*- coding: utf-8 -*-

"""
Copyright (c) Microsoft Corporation.
Licensed under the MIT License.
"""

import unittest

from dapr.clients.grpc._request import InvokeServiceRequestData
from dapr.proto import common_v1


class InvokeServiceRequestDataTests(unittest.TestCase):
    def test_bytes_data(self):
        # act
        data = InvokeServiceRequestData(data=b'hello dapr')

        # arrange
        self.assertIsNotNone(data.rawdata)
        self.assertEqual('', data.rawdata.type_url)
        self.assertEqual(b'hello dapr', data.rawdata.value)
        self.assertEqual('application/json; charset=utf-8', data.content_type)

    def test_proto_message_data(self):
        # arrange
        fake_req = common_v1.InvokeRequest(method="test")

        # act
        data = InvokeServiceRequestData(data=fake_req)

        # assert
        self.assertIsNotNone(data.rawdata)
        self.assertEqual(
            'type.googleapis.com/dapr.proto.common.v1.InvokeRequest',
            data.rawdata.type_url)
        self.assertIsNotNone(data.rawdata.value)
        self.assertIsNone(data.content_type)

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            data = InvokeServiceRequestData(data="invalid_data")
            self.assertIsNone(data, 'This should not be reached.')


if __name__ == '__main__':
    unittest.main()