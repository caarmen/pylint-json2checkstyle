"""
Tests for json2checkstyle
"""
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
    <error column="4" line="49" message="Disallowed name &quot;foo&quot;" severity="info" source="C0104:disallowed-name"/>
    <error column="4" line="49" message="Unused variable 'foo'" severity="warning" source="W0612:unused-variable"/>
  </file>
  <file name="myproject/apps/myapp/views.py">
    <error column="0" line="1" message="Missing module docstring" severity="info" source="C0114:missing-module-docstring"/>
    <error column="31" line="64" message="Unused argument 'request'" severity="warning" source="W0613:unused-argument"/>
    <error column="4" line="64" message="Method could be a function" severity="warning" source="R0201:no-self-use"/>
  </file>
</checkstyle>
"""

        actual_checkstyle_output = json2checkstyle(json_input)
        assert actual_checkstyle_output == expected_checkstyle_output
