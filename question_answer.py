import os
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 预定义问题列表（key），对应答案是字典直接存储的或者文件名，交由下面判断处理
qa_dict = {
    "你好": "你好！有什么可以帮您？",
    "你是谁": "我是一个问答机器人。",
    "今天天气怎么样": "weather.txt",  # 长答案放文件里
    "How are you?": "I'm fine, thank you!",
    "What is your name?": "your_name.txt",  # 文件中答案
    "What is the weather today?": "weather.txt",  # 和中文天气问题共用天气文件
}

# 答案文件所在目录
ANSWER_DIR = "answers"  # 这一建立这个文件夹，存储对应的答案。

def get_answer_from_file(filename):
    path = os.path.join(ANSWER_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        return f"读取答案文件失败: {str(e)}"

def get_answer(ans):
    # 判断答案是文件名还是直接文本
    if isinstance(ans, str) and ans.endswith('.txt'):
        return get_answer_from_file(ans)
    else:
        return ans

def jieba_tokenizer(text):
    return list(jieba.cut(text))

# 载入所有问题
questions = list(qa_dict.keys())
# 词袋模型向量化
vectorizer = CountVectorizer(tokenizer=jieba_tokenizer)
X = vectorizer.fit_transform(questions)

def answer_question(query):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, X).flatten()
    # 收集所有匹配条目
    all_matches = []
    for i in range(len(questions)):
        q = questions[i]
        ans_key = qa_dict[q]
        sim = similarities[i]
        all_matches.append((q, ans_key, sim))
    # 按相似度降序排序
    all_matches.sort(key=lambda x: x[2], reverse=True)
    # 相似度最高的条目
    top_q, top_ans_key, top_sim = all_matches[0]
    top_ans = get_answer(top_ans_key)
    return all_matches, (top_q, top_ans, top_sim)

# 持续对话模式
while True:
    query = input("请输入您的问题（输入 '退出' 结束对话）：")
    if query.lower() == '退出':
        print("感谢您的使用，再见！")
        break
    all_matches, top_match = answer_question(query)
    print(f"\n查询：{query}")
    print("\n全部匹配：")
    for q, ans_key, sim in all_matches:
        ans_text = get_answer(ans_key)
        print("问题:", q, "\t相似度:{:.3f}".format(sim), "\t答案:", ans_text)
    print("\n相似度最高的问题和答案：")
    print("问题:", top_match[0])
    print("相似度: {:.3f}".format(top_match[2]))
    print("答案:", top_match[1])
