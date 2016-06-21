# 文档

如何为项目写文档、用什么写文档、如何方便的管理/更新文档，这是很多技术人员都要经常面对的一些问题。根据个人经验，程序开发类工作中我们涉及到的文档可能主要包括下面几类，
* 函数/类的接口说明文档， 比如 XXX Framework API Documentation
* 服务端接口说明文档，比如 Web Service API, Restful API 等
* 使用指南、手册等说明文档，比如 Getting Start XXX, XXX Tutorial, XXX Guideline, XXX Manual 等
* 设计相关文档，比如 数据库 ER 图、类图、时序图等（Enterprise Architect）

## 相关工具/平台

下面，我们将分别介绍一些常用的相关工具/平台

### 使用指南、手册等说明文档

此类文档内容多以大段文字说明为主，一般按章节进行内容组织，随着项目的不断成熟、演进，很多成熟项目的文档都会有相当篇幅；于此同时，出于格式、排版等需求，逐步形成了多种标记语言标准，常见的比如 TeX, DocBook, Markdown, reStructuredText, AsciiDoc 等。目前互联网项目中主要流行 Markdown, reStructuredText, AsciiDoc 等轻量级标记语言，Tex、DocBook 过于复杂，reStructuredText 主要在 Python 开发者中流行，Org-mode 主要以 Emacs 用户为主，Markdown 最为流行（由于 Markdown 过于简单，目前几大组织/公司分别定义了自己的 Markdown 扩展语法，比如 GitHub Flavored Markdown，MultiMarkdown，Markdown Extra，Pandoc Markdown 等）。

扩展阅读：
* [Comparison of document markup languages](https://en.wikipedia.org/wiki/Comparison_of_document_markup_languages)
* [Lightweight markup language](https://en.wikipedia.org/wiki/Lightweight_markup_language) - 其中有好几种都是 Markdown 的方言；毛主席教导我们要辩证的去看问题，多种方言同时出现一方面反映出以简为美起家的 Markdown 是如此流行，另一方面也显示出 Markdown 扩展语法标准混乱的无奈。
* [Lightweight Markup: Markdown, reStructuredText, MediaWiki, AsciiDoc, Org-mode](http://hyperpolyglot.org/lightweight-markup)

#### ReST（reStructuredText）

* [Sphinx Documentation](http://sphinx-doc.org/)，可能是 ReST（reStructuredText） 系的代表项目了吧，Python 开发，由于语法简单、功能强大，非常多的项目都使用 Sphinx 来生成项目文档（[感受下?](http://sphinx-doc.org/examples.html)），跟他一起出现的还有 [Read The Docs](https://readthedocs.org/)（开源文档生成的托管平台和社区，同时支持 reStructuredText 格式以及 Markdown 格式） 这位兄弟，关于他们之间的关系，可以[看下这里](https://coderwall.com/p/vemncg/what-is-the-difference-rest-docutils-sphinx-readthedocs)；相关 PHP 项目示例，
    * [Guzzle](http://guzzle3.readthedocs.org/)，[源码](https://github.com/guzzle/guzzle/tree/v3.8.1/docs)
    * [CakePHP Cookbook 3.x](http://book.cakephp.org/3.0/en/index.html)

#### Markdown

由于 [Markdown](http://daringfireball.net/projects/markdown/) 简单易读，只需要普通的文本编辑器就能够编辑，语法更是简单到每个人都可以在数分钟内学会，因此，作为一门 2004 年才被发明出来的轻量级标记语言，Markdown 很快便得到了诸如 [Github](https://github.com)，[reddit](https://www.reddit.com/), [Stack Exchange](http://stackexchange.com/), [Bitbucket](http://sourceforge.net/) 等大量网站的支持。而伴随着 Github 旋风横扫整个开源界， git + Github + Markdown + Jekyll 组合更是成为互联网时代大量科技写作者甚至小部分文艺青年的主力生产力平台。

* [Jekyll](https://jekyllrb.com/) - 不仅仅可以生成静态博客站点，Jekyll 同样适用于文档内容生成，Wista（一家企业视频托管服务提供商）[在这里](http://wistia.com/blog/jekyll-for-documentation)分享了他们基于 Jekyll 的文档管理经验，你可以[点这里先睹为快](http://wistia.com/doc)（[源码](https://github.com/wistia/wistia-doc)）。下面列举了 Jekyll 文档其他相关主题，
    * [Jekyll Documentation Theme](https//github.com/tomjohnson1492/documentation-theme-jekyll/)，示例：[Official Doc](http://idratherbewriting.com/documentation-theme-jekyll)
    * [Jekyll-docs-template](https://github.com/bruth/jekyll-docs-template/)，示例：[Official Doc](http://bruth.github.io/jekyll-docs-template/)，[ModelTree](http://modeltree.harvest.io/ref/lookup-syntax.html)
* [MkDocs](http://www.mkdocs.org/) - 根据 Markdown 文档生成静态网站，Python 语言开发，
    * [SlimFramework v2 Doc](http://docs.slimframework.com/) - 个人常用的一个 PHP 轻量级框架，小内核 + Composer 包，可玩性很高~ 类似的可选项还有 [Silex](http://silex.sensiolabs.org/) 和 [Lumen](https://lumen.laravel.com/)
    * [小米开放平台文档中心](http://dev.xiaomi.com/docs/)
    * [Flask API Doc](http://www.flaskapi.org/) - 另外一款轻量级 Python Web 开发框架
* [GitBook](https://github.com/GitbookIO/gitbook) - 除了 Markdown，GitBook 还支持另外一种与 Markdown 很类似但功能更丰富的标记语言 AsciiDoc；GitBook 除了提供基于 node.js 开发的可供本地运行的命令行版本外，还提供了[在线托管服务](https://www.gitbook.com/)。
    * [GitBook Multi-Languages support](http://help.gitbook.com/format/languages.html)
* [Peach](https://peachdocs.org/) - 国人基于 Go 语言开发的一款支持多语言、实时同步以及全文搜索功能的 Web 文档服务器。赞一个~，使用示例，
    * [Peach 文档](https://peachdocs.org/docs) - Peach 官方文档
    * [Gogs 文档](https://gogs.io/docs) - 国人基于 Go 语言开发的类 Gitlab 服务器，界面比较小清新哦~

下面的表格对比了几款支持 Markdown 的主流文档工具之间主要特性的区别（实际区别可能与我所理解的有偏差）：

|名称           |自助托管----|多语言文档|实时同步|静态 HTML |多版本      |
|:------------:|:---------:|:-------:|:-----:|:--------:|:---------:|
|Read The Docs |✗          |✓        |✓      |✓         |✓          |
|Peach         |✓          |✓        |✓      |✓（可缓存）|[计划中](https://peachdocs.org/docs/intro/roadmap)|
|Mkdocs        |✓          |✗        |✗     |✓         |✗          |
|GitBook       |✓          |✓        |✓      |✓         |✗          |
|Jekyll        |✓          |✓（插件） |✓      |✓         |✓（不完美）  |

#### AsciiDoc

[AsciiDoc](http://asciidoc.org/) 最初基于 Python 开发，其基本语法跟 Markdown 类似，例如以 = 开头作为标题、以 * 号开头作为列表项等，详细的语法说明可以[看这里](http://powerman.name/doc/asciidoc)，但 AsciiDoc 比 Markdown 支持更多的格式，比如表格、文件包含等，同时 AsciiDoc 是 O'Reilly 的 [Atlas 在线出版平台](http://chimera.labs.oreilly.com/) 的推荐语言，相当大部分的 [Git 官方文档](https://git.wiki.kernel.org/index.php/AsciiDoc)都使用了 AsciiDoc 格式。

扩展阅读：
* [AsciiDoctor](http://asciidoctor.org/) - 2013 年发布，是 AsciiDoc 基于 Ruby 语言的实现，主要[在 GitHub 使用](http://asciidoctor.org/news/2013/01/30/asciidoc-returns-to-github/)。

#### DocBook

* [DocBook](http://www.docbook.org/) 比 HTML 语言还早一年（1992 年）出现的 XML 系标记语言，可以非常方便的生成其他文件格式，比如 HTMl、PDF、CHM 等，开源界使用 DocBook 的项目非常多，比如大家耳熟能详的一些项目，[Linux Kernel](https://www.kernel.org/)、[FreeBSD](http://www.freebsd.org/)、[PostgreSQL](http://www3.uk.postgresql.org/users-lounge/docs/)、[O'Reilly Media](http://www.oreilly.com/)、[OpenStack](http://docs.openstack.org/)，[PHP 的官方文档](http://www.php.net/download-docs.php)也用的它哦，更多项目和组织列表可以[看这里](http://wiki.docbook.org/WhoUsesDocBook)；不过纯 PHP 相关项目使用 Docbook 的较少，毕竟使用 XML 来写文档门槛有点高 :sunglasses:，项目示例，
    * [PHPUnit Documentation](https://phpunit.de/manual/5.1/en/index.html)，[源码](https://github.com/sebastianbergmann/phpunit-documentation)

#### Tex

[Tex](http://tug.org/) 是由 [Donald Knuth](https://zh.wikipedia.org/wiki/Donald_Knuth) 创造的基于低级编程语言的电子排版系统，利用 TeX 能够对文章进行十分精美的排版，TeX 提供了一套功能强大并且十分灵活的排版语言，同时 TeX 系统是公认的数学公式排得最好的系统。

* [LaTeX](https://latex-project.org/) - LaTeX（发音为“Lah-tech”或“Lay-tech”）是由 [Leslie Lamport](https://zh.wikipedia.org/wiki/Leslie_Lamport) 开发的当今世界上最流行和使用最为广泛的TeX宏集。 把 LaTeX 放到最后是由于 TeX 语法的高门槛，导致除了专业的科学研究、出版领域，除了我们敬仰的那些大神们，在偏工程/应用类的普通码农界中没有真正大规模流行开来。

### 函数/类的接口说明文档
* [PHPDoc](http://www.phpdoc.org/)，写 PHP 的都应该知道这个哈，嘿嘿。示例，
    * [Zend Framework 2.4 API Documentation](http://framework.zend.com/apidoc/2.4/)
    * [Offical Demo with Clean2 theme](http://demo.phpdoc.org/Clean2/)
* [Sami](https://github.com/FriendsOfPHP/Sami)，Symfony 框架使用的文档生成工具，示例，
    * [Symfony 3.0 API](http://api.symfony.com/3.0/index.html)
    * [Composer API](https://getcomposer.org/apidoc/master/index.html)
* [Doxygen](http://www.stack.nl/~dimitri/doxygen/)，超级老牌文档生成工具了，除了 PHP 外还支持其他 N 种编程语言
* [phpDox](http://phpdox.de/)
* [Apigen](http://www.apigen.org/)
    * [Amazon AWS SDK for PHP 3.x](http://docs.aws.amazon.com/aws-sdk-php/v3/api/)
    * [CakePHP API Docs](http://api.cakephp.org/3.1/)


### 服务端接口说明文档
* [Swagger](http://swagger.io/), [Demo](http://petstore.swagger.wordnik.com/)
* [Apiary](https://apiary.io) - （**推荐**）Apiary.io平台具有协同设计、即时API模拟、快速生成源码、自动测试和代码调试的开源设计工具，最重要的是可以在线模拟测试，因为该平台具备模拟服务器测试服务，可以把设计好的程序在线测试、验证。
* [Apidoc](http://apidocjs.com/), [Demo](http://apidocjs.com/example/) 
* [Slate](https://github.com/tripit/slate) - 创建好看的 API 文档，Travis-CI, Appium 等项目使用中，更多例子：[Examples of Slate in the Wild](https://github.com/tripit/slate#examples-of-slate-in-the-wild)
* [JSON-Schema](http://json-schema.org/)
* [prmd](https://github.com/interagent/prmd) - JSON Schema tools and doc generation for HTTP APIs
* [如何编写 API 的文档？](http://segmentfault.com/q/1010000002523945)


### 设计相关文档
