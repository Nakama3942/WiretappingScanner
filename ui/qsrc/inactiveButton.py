#  Copyright © 2023 Kalynovsky Valentin. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from PyQt6.QtWidgets import QPushButton

class InactiveButton(QPushButton):
    # Used in the connection button group in case there are no devices to connect, since this
    # property becomes True only in this case. This property is needed for the buttons in the
    # connection system to work correctly, on which the optimization of the program depends.
    trouble = False

    def mousePressEvent(self, event):
        if self.isChecked():
            event.ignore()
        else:
            super().mousePressEvent(event)
