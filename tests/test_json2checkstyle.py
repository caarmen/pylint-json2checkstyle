"""
Tests for json2checkstyle
"""
from xml.dom import minidom

from pylint_json2checkstyle.checkstyle_reporter import json2checkstyle


class TestClass:
    """
    Tests for json2checkstyle
    """

    def test_json2checkstyle(self):
        """
        Verify that the checkstyle output created from a json input is as expected
        """
        json_input = """
[
    {
        "type": "convention",
        "module": "myproject.apps.myapp.service",
        "obj": "get_myapp_list",
        "line": 49,
        "column": 4,
        "endLine": 49,
        "endColumn": 7,
        "path": "myproject/apps/myapp/service.py",
        "symbol": "disallowed-name",
        "message": "Disallowed name \\"foo\\"",
        "message-id": "C0104"
    },
    {
        "type": "warning",
        "module": "myproject.apps.myapp.service",
        "obj": "get_myapp_list",
        "line": 49,
        "column": 4,
        "endLine": 49,
        "endColumn": 7,
        "path": "myproject/apps/myapp/service.py",
        "symbol": "unused-variable",
        "message": "Unused variable 'foo'",
        "message-id": "W0612"
    },
    {
        "type": "convention",
        "module": "myproject.apps.myapp.views",
        "obj": "",
        "line": 1,
        "column": 0,
        "endLine": null,
        "endColumn": null,
        "path": "myproject/apps/myapp/views.py",
        "symbol": "missing-module-docstring",
        "message": "Missing module docstring",
        "message-id": "C0114"
    },
    {
        "type": "warning",
        "module": "myproject.apps.myapp.views",
        "obj": "MyQuerySet._unused_function",
        "line": 64,
        "column": 31,
        "endLine": 64,
        "endColumn": 38,
        "path": "myproject/apps/myapp/views.py",
        "symbol": "unused-argument",
        "message": "Unused argument 'request'",
        "message-id": "W0613"
    },
    {
        "type": "refactor",
        "module": "myproject.apps.myapp.views",
        "obj": "MyQuerySet._unused_function",
        "line": 64,
        "column": 4,
        "endLine": 64,
        "endColumn": 24,
        "path": "myproject/apps/myapp/views.py",
        "symbol": "no-self-use",
        "message": "Method could be a function",
        "message-id": "R0201"
    }
]
"""
        expected_checkstyle_output = """<?xml version="1.0" ?>
<checkstyle>
  <file name="myproject/apps/myapp/service.py">
    <error line="49" column="4" message="Disallowed name &quot;foo&quot;" source="C0104:disallowed-name" severity="info"/>
    <error line="49" column="4" message="Unused variable 'foo'" source="W0612:unused-variable" severity="warning"/>
  </file>
  <file name="myproject/apps/myapp/views.py">
    <error line="1" column="0" message="Missing module docstring" source="C0114:missing-module-docstring" severity="info"/>
    <error line="64" column="31" message="Unused argument 'request'" source="W0613:unused-argument" severity="warning"/>
    <error line="64" column="4" message="Method could be a function" source="R0201:no-self-use" severity="warning"/>
  </file>
</checkstyle>
"""

        actual_checkstyle_output = json2checkstyle(json_input)
        expected_checkstyle_document = minidom.parseString(expected_checkstyle_output)
        actual_checkstyle_document = minidom.parseString(actual_checkstyle_output)
        assert actual_checkstyle_document.toprettyxml() == expected_checkstyle_document.toprettyxml()
