Test other elements in Sphinx
===================================

Inline markups
--------------------

- standard
- *emphasis*
- **strong emphasis**
- ``code``

Lists
--------------

- Test
- Test

  - Test

    - Test

      - Test

- Test

1. Test
2. Test

   1. Test

      1. Test

term
    definition

    more definition

.. cspell:disable

Quotes
---------

    Lorem ipsum dolor sit amet Duo consetetur molestie diam est eirmod facer illum diam. Esse est voluptua accusam eleifend ut voluptua nonumy clita nonumy dolor et tempor amet accusam est et sit.

    -- from a generator

.. cspell:enable

Tables
-------------

.. csv-table:: Simple Table
    :widths: auto
    :header-rows: 1

    Column 1, Column 2, Column 3
    Value, Value, Value

.. csv-table:: Extreme Table
    :widths: auto
    :header-rows: 1

    Label, Long Long Long Long Long Label
    Long Long Long Long Long Long Long Long Long Long Long Long Long Long Long Long Long Long Value, Value

Links
------------------

- `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
