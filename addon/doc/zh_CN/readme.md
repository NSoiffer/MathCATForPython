# MathCAT #

* 作者: 尼尔·索伊弗尔(Neil Soiffer)
* NVDA 兼容性： 2018.1 或更高版本（未在早期版本中测试）
* 下载 [稳定版][1]

MathCAT is designed to eventually replace MathPlayer because MathPlayer is
no longer supported. MathCAT generates speech and braille from MathML. The
speech for math produced by MathCAT is enhanced with prosody so that it
sounds more natural. The speech can be navigated in three modes using the
same commands as MathPlayer. In addition, the navigation node is indicated
on a braille display. Both Nemeth and UEB technical are supported.

MathCAT 有许多控制语音、导航和盲文的配置选项。其中许多可以在 MathCAT 设置对话框中设置 （可从 NVDA
首选项菜单中找到）。有关这些设置的更多信息，请参阅 [MathCAT
文档](https://nsoiffer.github.io/MathCAT/users.html)。该文档包含指向 [MathCAT
导航命令表](https://nsoiffer.github.io/MathCAT/nav-commands.html) 的链接。

注意： MathCAT 是一个用于从 MathML 生成语音和盲文的通用库。除了 NVDA 之外，其他 AT （辅助工具）项目也在使用。有关
MathCAT 项目的常规信息，请参阅 [MathCAT 文档主页](https://nsoiffer.github.io/MathCAT)。


谁应该使用 MathCAT：

* 那些需要高质量 Nemeth 码盲文的人 （MathPlayer 的 Nemeth 码基于 liblouis 的 Nemeth
  码一代，有许多技术上难以修复的重大错误）。
* Those who need UEB technical braille, CMU (Spanish/Portuguese), German
  LaTeX, ASCIIMath, or Vietnamese braille
* 那些想要尝试最新技术并愿意通过报告 Bug 来提供帮助的人
* 那些用 Eloquence 合成器的人

谁不应该使用 MathCAT：

* Anyone who uses MathPlayer with a language that is not yet supported by
  MathCAT (translations exist for Chinese (Traditional), Spanish, Indonesian
  and Vietnamese; translations will be coming in the future) and are not
  comfortable with speech in one of the supported languages.
* 任何喜欢 Access8Math 而不是 MathPlayer 的人 (需要使用语音或其他更多功能的人)

MathCAT 的语音规则还没有 MathPlayer 的规则那么全面——这可能是坚持使用 MathPlayer 的另一个原因。MathCAT 被用作
MathML 4 思想的测试平台，它允许作者表达他们的意图，以便能够正确地说出不明确的符号，而不是猜测。我没有添加太多规则，因为 MathCAT
的体系结构以使用和推断作者意图为中心，这些还没有完全解决。

## MathCAT 更新日志

### Version 0.6.3
* All the language and braille Rule files are zipped up per directory and unzipped on demand.
  * This currently saves ~5mb when Rules.zip is unzipped, and will save even more as more languages and braille codes are added.
  * This is in preparation for MathCAT being built into NVDA 2024.3
* Added new preference `DecimalSeparator`.
  * The default value is `Auto`, with other values being ".", ",", and "Custom". The first three values set `DecimalSeparators` and `BlockSeparators`.
  * `Auto` sets those preferences based on the value of the `Language` pref. For some language such as Spanish, `,` is used in some countries and `.` is used in others. In this case, it is best to set the language to also include the country code (e.g, `es-es` or `es-mx`) to ensure the right value is used.
* Added Swedish to supported languages.
* Added more Unicode chars to include both all Unicode chars marked as "Sm" and those with a mathclass (except Alphabetic and Glyph classes) in the Unicode standard.
* After changing how prefs work in a previous version, I forgot to change `MathRate` and `PauseFactor` to be numbers, not strings.
* Fixed bug in the braille Rules (missed change from earlier) where a third argument should have been given to say to look in the _Braille_ `definitions.yaml` files and not the speech ones when looking up the value of a definition.
* Cleaned up use of `definitions.yaml`.
* Fixed some bugs in the MathML cleanup for "," decimal separators.
* Found a bug in braille highlighting when nothing is highlighted (maybe never happens which is why I didn't see it in practice?)
* Fixed "Describe" mode so that it works -- it is still very minimal and probably not useful yet
* Fixed minimum supported version

### Version 0.5.6
* Added Copy As... to the MathCAT dialog (in the "Navagation" pane).
* Fixed a bug where the language reverted to English when changing speech
  styles.
* Fixed a bug with navigation and braille
* Fixed some Asciimath spacing problems.
* Improved chemistry recognition
* Updated MathCAT to new BANA Nemeth chemistry spec (still only single line
  and special case style/font changes not handled)
* Fix a crash when non-ASCII digits (e.g., bold digits) are used in numbers
* Don't use italic indicators in braille codes when the math alphanumeric
  italic chars are used
* Some other smaller bug fixes that weren't reported by users

### 版本 0.5.0
* 添加了德语 LaTeX 盲文代码。与其他盲文代码不同，这会生成 ASCII 字符，并使用当前盲文输出表将字符转换为盲文。
* 增加了（实验） ASCII Math 盲文码。与 LaTeX 盲文代码一样，它生成 ASCII 字符，并使用当前盲文输出表将字符转换为盲文。
* 添加了`CopyAs`首选项，支持在关注 MathML 时使用 ctrl+C 复制为 MathML、LaTeX 或 ASCII
  Math（如前所述）。将复制当前关注的节点。注意：这仅列在 prefs.yaml 文件中，并且尚未在 “MathCAT首选项” 对话框中公开。

### 版本 0.4.2
* 修复了语音变化且 MathCAT 语言为“自动”时的语言切换问题
* 添加了更多 $Impairments 检查，以在未为盲人设置时提高阅读能力
* Nemeth:修复了“~”不是 mrow 的一部分时的问题
* UEB: character additions, "~" spacing fix if prefix, xor fix,
* 对重音元音的 MathML 清理(主要针对越南语)
* 首选项读取/更新代码的重大重写，速度大大加快--添加了`CheckRuleFiles`前缀以控制检查哪些文件进行更新
* Added two new interface calls -- enables setting the navigaton location
  from the braille cursor (not part of MathCAT addon yet)

### 版本 0.3.11
* 升级到 python 3.11，并验证可以与 NVDA 2024.1 一起工作
* 修复越南语盲文和语音中的错误，主要用于化学。
* 修复当盲文代码和相关语言不匹配时停止工作的问题（特别是越南盲文和越南语语音）
* 修复了 HTML 标记内部的空白错误
* 改进了罗马数字检测


### 版本 0.3.9
* 增加了繁体中文翻译（感谢 Hon-Jang Yang）
* Fixed bug with navigating into the base of a scripted expression that has
  parenthesis
* 显著改变了空白的处理方式。这主要影响盲文输出（空白和“省略”检测）。
* 完善了对化学的识别
* 添加化学示例后产生的UEB盲文修复
* UEB 修复了在某些情况下添加辅助括号的问题


### 版本 0.3.8
Braille: * Dialog has been internationalized for several languages (many
thanks to the translators!)  * Initial implementation of CMU -- the braille
code used in Spanish and Portuguese speaking countries * Fix some UEB bugs
and added some characters for UEB * Significant improvements to Vietnamese
braille

Other fixes: * Change relative rate dialog slider to have a maximum value of
100% (now only allows setting slower rates). Also, added step sizes so it is
easier to raise/lower the rate significantly.  * Fix eSpeak bug that
sometimes cut off speech when the relative rate was changed * Improvements
to Vietnamese speech * Fixed bug with OneCore voices saying "a" * Fixed some
navigation bugs when `AutoZoomOut` is False (not the default)  * Fix
updating around language changes and some other dialog changes so they take
effect immediately upon clicking "Apply" or "OK".  * Added an "Use Voice's
Language" option so that out of the box, MathCAT will speak in the right
language (if there is a translation)  * Several improvements for cleaning up
poor MathML code

### 版本 0.3.3
This release has a number of bug fixes in it. The major new features and bug
fixes are: * Added Spanish Translation (thanks to Noelia Ruiz and María Allo
Roldán)  * Modified navigation so that it starts zoomed in one level * Added
cntrl+alt+arrow as a way to navigate tabular structures. These keys should
be more memorable because they are used for table navigation in NVDA.  *
Worked around NVDA bug for eSpeak voices that caused them to slow down when
the relative MathRate was set to be slower than the text speech rate.  *
Worked around a OneCore voice problem so that they will speak the long 'a'
sound.

语音有一些小的调整， Nemeth 码和 UEB 有一些错误修复。

注： 现在可以选择将越南的盲文标准作为盲文输出。这仍然是一项正在进行的工作，并且存在太多的 bug，不能用于测试之外的其他用途。我预计下一个
MathCAT 版本将包含一个可靠的实现。

### 版本 0.2.5
* 进一步化学改进
* 对 Nemeth 码的修复：
* * Added "omission" rules
* * Added some rules for English Language Indicators
* * Added more cases where the Mulitpurpose indicator is needed
* * Fixes related to Nemeth and punctuation

### 版本 0.2
* 大量错误修复
* 改善语音
* 一个首选项用于控制暂停持续时间 （适用于数学中相对语速的更改）
* 支持识别并是当说出化学符号
* 印尼语和越南语翻译

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
