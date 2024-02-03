日本語のテストページ
=====================

福沢諭吉「学問のすすめ」

「天は人の上に人を造らず人の下に人を造らず」と言えり。されば天より人を生ずるには、万人は万人みな同じ位にして、生まれながら貴賤上下の差別なく、万物の霊たる身と心との働きをもって天地の間にあるよろずの物を資り、もって衣食住の用を達し、自由自在、互いに人の妨げをなさずしておのおの安楽にこの世を渡らしめ給うの趣意なり。

ヘッダ2
-----------------

されども今、広くこの人間世界を見渡すに、かしこき人あり、おろかなる人あり、貧しきもあり、富めるもあり、貴人もあり、下人もありて、その有様雲と泥との相違あるに似たるはなんぞや。

ヘッダ3
..................

その次第はなはだ明らかなり。『実語教』に、「人学ばざれば智なし、智なき者は愚人なり」とあり。

ヘッダ4
```````````````````

されば賢人と愚人との別は学ぶと学ばざるとによりてできるものなり。また世の中にむずかしき仕事もあり、やすき仕事もあり。

ヘッダ5
''''''''''''''''''

そのむずかしき仕事をする者を身分重き人と名づけ、やすき仕事をする者を身分軽き人という。

ヘッダ 6
^^^^^^^^^^^^^

すべて心を用い、心配する仕事はむずかしくして、手足を用うる力役はやすし。

Inline markup
--------------------

- 標準 standard
- *強調* *emphasis*
- **さらに強調** **strong emphasis**
- ``コード`` ``code``

リスト
--------------

- テスト
- テスト

  - テスト

    - テスト

      - テスト

- テスト

1. テスト
2. テスト

   1. テスト

      1. テスト

term
    definition

単語
    説明

    もう少し説明

.. cspell:disable

引用
------------

    吾輩は猫である。名前はまだ無い。
    どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。

    -- 夏目漱石「吾輩は猫である」

.. cspell:enable

表
-------------

.. csv-table:: 単純な表
    :widths: auto
    :header-rows: 1

    列1,列2,列3
    テスト,テスト,テスト

.. csv-table:: 極端な表
    :widths: auto
    :header-rows: 1

    長い列,タイトルが長いだけの列
    長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章 長い文章,2

リンク
------------------

- `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

各種メッセージ
-------------------

.. attention:: ``attention`` のテスト

.. caution:: ``caution`` のテスト

.. danger:: ``danger`` のテスト

.. error:: ``error`` のテスト

.. hint:: ``hint`` のテスト

.. important:: ``important`` のテスト

.. note:: ``note`` のテスト

.. tip:: ``tip`` のテスト

.. warning:: ``warning`` のテスト

.. todo:: ``todo`` のテスト

.. versionadded:: 1.2.3
    ``versionadded`` のテスト

.. versionchanged:: 1.2.3
    ``versionchanged`` のテスト

.. deprecated:: 1.2.3
    ``deprecated`` のテスト

.. seealso:: ``seealso`` のテスト

ソースコード
--------------------

.. code-block:: c++
    :caption: 色々な要素を含んだ C++ コード

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
    :caption: 色々な要素を含んだ Python コード

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

数式
-------------

- 基本的な記号

  .. math::

      \sum_{n=1}^\infty \frac{1}{n^2}
      = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \ldots
      = \frac{\pi^2}{6}

- ``\bm`` によるベクトル表記

  .. math::

      \bm{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}

- 横に長い数式

  .. math::

      1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
      + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20
      + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 38 + 29 + 30

- 等号の位置揃え

  .. math::

      a &= 1 \\
      b &= 12345 \\
      \bm{c} &= \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}

PlantUML
----------------

.. uml::

    activate クライアント
    クライアント -> サーバ ++ : リクエスト
    return レスポンス
