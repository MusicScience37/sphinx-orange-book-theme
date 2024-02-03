Test of source codes
===========================

.. code-block:: c++
    :caption: An example of source code in C++.

    #include <iostream>

    template <typename T>
    class Example {
    public:
        /*!
         * \brief Construct.
         *
         * \param[in] var var.
         */
        Example(T var) : var_(var) {}

        /*!
         * \brief Get var.
         *
         * \return var.
         */
        [[nodiscard]] const T& var() const { return var_; }

    private:
        //! var.
        T var_;
    };

    int main() {
        Example<int> ex(5);
        int res = ex.var();
        return 0;
    }

.. code-block:: python
    :caption: An example of source code in Python.

    """Test of a code block."""

    import pathlib
    import typing

    THIS_DIR = pathlib.Path(__file__).absolute().parent


    class Example:
        """A class for test of a code block."""

        def __init__(self, value: typing.Optional[int] = None) -> None:
            if value is None:
                value = 12345
            self._value = value

        @property
        def value(self) -> int:
            """Get the value."""
            return self._value


    if __name__ == "__main__":
        main()
