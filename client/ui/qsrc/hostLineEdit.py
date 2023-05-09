"""
Specifies the correct IP address of the network host to find connected devices to the network.
\n
Copyright © 2023 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

class HostLineEdit(QLineEdit):
    """
    A class that describes the rules for entering a network host.
    """
    def __init__(self, parent=None):
        super(HostLineEdit, self).__init__(parent)

        # Create a validator to restrict user input
        self.setValidator(
            QRegularExpressionValidator(
                QRegularExpression(
                    r"^25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d$"
                ), self
            )
        )

    # Initially, it was planned that the field would be filled with a full IP address
    # like 192.168.XXX.1, where the user could enter text only between the second and
    # third commas, but this logic could not be implemented ... I had to move the unchanged
    # parts into QLabel, but I hope that someday I will finish it.
