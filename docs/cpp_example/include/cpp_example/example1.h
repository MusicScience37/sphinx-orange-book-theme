/*!
 * \file
 * \brief An example of C++ header.
 */
#pragma once

namespace cpp_example::example1 {

/*!
 * \brief A class.
 *
 * \tparam Args Arguments.
 */
template <typename ... Args>
class Example1 {
public:
    /*!
     * \brief Constructor.
     *
     * \tparam InputArgs Types of arguments.
     * \param[in] args Arguments.
     */
    template <typename ... InputArgs>
    Example1(InputArgs&& ... args) {}

    /*!
     * \brief Get a value.
     *
     * \param[in] arg1 Argument.
     * \param[in] arg2 Argument.
     * \return Result.
     */
    [[nodiscard]] int get_value(int arg1, int arg2) const noexcept;
};

/*!
 * \brief A class.
 */
class Example2 {
public:
    /*!
     * \brief Constructor.
     *
     * \tparam Args Types of arguments in Example1 class.
     * \param[in] arg Argument.
     */
    template <typename ... Args>
    Example2(Example1<Args...>& arg);
};

}
