# 🤖 问答机器人 README

## 项目简介

这是一个简单的问答机器人，能够根据用户输入的问题返回相应的答案。该机器人使用了中文分词库 `jieba` 和 `scikit-learn` 库中的词袋模型和余弦相似度计算来匹配用户的问题与预定义的问题列表。

## 功能

- 🌐 支持中文和英文问题的回答。
- 📄 可以从文本文件中读取长答案。
- 📊 使用余弦相似度来找到与用户问题最相似的预定义问题。

## 依赖

- Python 3.x
- `jieba`：用于中文分词
- `scikit-learn`：用于文本向量化和相似度计算

## 安装

1. 确保已安装 Python 3.x。
2. 安装依赖库：
   ```bash
   pip install jieba scikit-learn
   ```

## 使用说明

1. 创建一个名为 `answers` 的文件夹，用于存储答案文件。
2. 在 `answers` 文件夹中创建以下文件：
   - `weather.txt`：存储天气相关的长答案。
   - `your_name.txt`：存储机器人的名字。

3. 在代码中，您可以根据需要修改 `qa_dict` 字典，添加或更改问题和答案。

4. 运行代码并输入问题，机器人将返回最相似的问题及其答案。

## 余弦相似度简介

余弦相似度是一种用于衡量两个向量之间相似度的指标。它通过计算两个向量夹角的余弦值来判断它们的相似程度。值的范围在 -1 到 1 之间，值越接近 1，表示两个向量越相似；值越接近 -1，表示两个向量越不相似。

公式如下：

\[
\text{cosine\_similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}
\]

其中，\(A\) 和 \(B\) 是两个向量，\(\cdot\) 表示点积，\(\|A\|\) 和 \(\|B\|\) 是向量的模。

## 示例

```python
query = "今天天气如何"
all_matches, top_match = answer_question(query)
print(f"查询：{query}")
print("\n全部匹配：")
for q, ans_key, sim in all_matches:
    ans_text = get_answer(ans_key)
    print("问题:", q, "\t相似度:{:.3f}".format(sim), "\t答案:", ans_text)
print("\n相似度最高的问题和答案：")
print("问题:", top_match[0])
print("相似度: {:.3f}".format(top_match[2]))
print("答案:", top_match[1])
```

## 贡献

欢迎任何形式的贡献！如果您发现了错误或有改进建议，请提交问题或拉取请求。🌟

## 许可证

本项目采用 MIT 许可证，详情请参阅 LICENSE 文件。📜

---

感谢您使用问答机器人！如有任何问题，请随时联系我。😊
