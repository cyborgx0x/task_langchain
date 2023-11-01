security_checks = [
    {
        "key": "SQL",
        "value": "Thực hiện truy vấn SQL an toàn qua ORM hoặc prepared statement.",
    },
    {"key": "Reflected XSS", "value": "Xây dựng bộ lọc XSS tốt hơn"},
    {
        "key": "Sensitive data exposed",
        "value": "Từ chối tất cả quyền truy cập vào file chứa thông tin nhạy cảm.",
    },
    {
        "key": "Directory listings",
        "value": "Từ chối tất cả quyền truy cập vào các thư mục nhạy cảm",
    },
    {
        "key": "Không có cơ chế chống bruteforce",
        "value": "Xây dựng cơ chế chống brute force.",
    },
    {
        "key": "Command Injection",
        "value": "Không dùng hàm system() hoặc exec() để thực thi các lệnh hệ thống dựa trên đầu vào từ người dùng. Sử dụng prepared statements để thực hiện các truy vấn cơ sở dữ liệu",
    },
    {
        "key": "Enums Usernames",
        "value": "Trả về thông báo chung. Nên sử dụng captcha sau 3 lần đăng nhập sai.",
    },
    {
        "key": "Broken Authentication",
        "value": "Xây dựng lại cơ chế quản lý cookie, session.",
    },
    {
        "key": "Clickjacking",
        "value": "Sử dụng X-Frame-Option, Content-Security-Policy header và Javascript chặn frame.",
    },
    {"key": "IDOR", "value": "Xác thực phân quyền các tham số đảm bảo yêu cầu."},
    {
        "key": "CSRF",
        "value": "Bổ sung cơ chế chống tấn công CSRF như sử dụng CSRF token.",
    },
    {
        "key": "Insecure browser caching",
        "value": "Trả về header Cache-Control với giá trị no-store",
    },
    {
        "key": "No rate-limiting",
        "value": "Yêu cầu điền captcha sau 3 lần đăng nhập sai liên tiếp.",
    },
    {
        "key": "Open redirect",
        "value": "Chỉ cho phép redirect về các URL thuộc domain của ứng dụng",
    },
    {
        "key": "Path Traversal",
        "value": "Validate input của người dùng trước khi xử lý, không nên chứa những ký tự đặc biệt.",
    },
    {
        "key": "Server directory traversal",
        "value": "Chặn truy cập vào file web config.",
    },
    {"key": "Wappalyzer Technology Detection", "value": "Cập nhật cài đặt bản vá mới."},
    {
        "key": "HTTP Missing Security Headers",
        "value": "Thêm header bảo mật vào trang web để ngăn chặn tấn công.",
    },
    {
        "key": "robots.txt endpoint prober",
        "value": "Kiểm tra và cấu hình robots.txt cẩn thận để đảm bảo chỉ ngăn cấm truy cập các phần bạn thực sự muốn bảo vệ.",
    },
    {
        "key": "WAF Detection",
        "value": "Đảm bảo cấu hình Web Application Firewall (WAF) cho phù hợp và kiểm tra cơ sở hạ tầng bảo mật định kỳ để phát hiện và ngăn chặn các cuộc tấn công.",
    },
    {
        "key": "Detect SSL Certificate Issuer",
        "value": "Kiểm tra và xác minh rằng chứng chỉ SSL được sử dụng cho trang web của bạn được phát hành bởi một tổ chức uy tín và đang còn hiệu lực.",
    },
    {
        "key": "SSL DNS Names",
        "value": "Kiểm tra SSL DNS Names để đảm bảo rằng tất cả tên miền liên quan đến trang web của bạn được bao gồm trong chứng chỉ SSL.",
    },
    {
        "key": "Wildcard TLS Certificate",
        "value": "Hãy đảm bảo rằng chứng nhận wildcard TLS còn hiệu lực, được bảo vệ riêng tư và được giám sát thường xuyên.",
    },
    {
        "key": "TLS Version – Detect",
        "value": "Sử dụng TLS phiên bản mới nhất,vô hiệu hóa phiên bản TLS cũ, kiểm tra cấu hình TLS để đảm bảo tính bảo mật. Theo dõi và cập nhật phiên bản TLS định kỳ.",
    },
    {
        "key": "Weak Cipher Suites Detection",
        "value": "Loại bỏ cipher suites yếu, sử dụng các cipher suites mạnh mẽ, cập nhật phần mềm TLS, và kiểm tra cấu hình TLS thường xuyên",
    },
    {
        "key": "Deprecated TLS Detection (TLS 1.1 or SSLv3)",
        "value": "Ngừng sử dụng TLS 1.1 và SSLv3, nâng cấp lên phiên bản TLS mới nhất, và kiểm tra cập nhật cấu hình TLS định kỳ để đảm bảo tính bảo mật liên tục.",
    },
    {
        "key": "Microsoft Azure Takeover Detection",
        "value": "Kiểm tra cấu hình bảo mật Azure, Sử dụng mật khẩu mạnh và xác thực hai yếu tố",
    },
    {
        "key": "favicon-detection",
        "value": "Đảm bảo rằng favicon của trang web của bạn được cài đặt và quản lý một cách đúng cách",
    },
    {
        "key": "Web cache poisoning",
        "value": "Kiểm tra lại việc sử dụng cache có cần thiết hay không.",
    },
    {
        "key": "GET request chứa thông tin nhạy cảm",
        "value": "Khi thông tin nhạy cảm được gửi, hãy sử dụng phương thức POST",
    },
    {
        "key": "Clockwork PHP dev tool enabled",
        "value": "Tắt chế độ debug trên môi trường product",
    },
    {
        "key": "Logic flaws",
        "value": "Limit request ,Xác thực rõ ràng khi đăng nhập bằng bên thứ 3 và tài khoản tự tạo",
    },
    {
        "key": "some-PIIs",
        "value": "Xác định và phân loại thông tin cá nhân (PII) quan trọng trong hệ thống, đảm bảo rằng dữ liệu PII được bảo vệ một cách an toàn thông qua việc sử dụng mã hóa và biện pháp bảo mật phù hợp.",
    },
    {"key": "Labda_403Bypass_slash", "value": "kiểm tra lại URL, quyền truy cập."},
    {
        "key": "api-linkfinder:relative_links",
        "value": "xem xét lại mã nguồn, liên kết tương đối đang được sử dụng một cách an toàn và chính xác. Kiểm tra xem liệu các đường dẫn tương đối đang được xử lý đúng cách và không có khả năng gây ra các lỗ hổng bảo mật",
    },
    {
        "key": "osint-extractor-emoji",
        "value": "kiểm tra và đánh giá xem việc sử dụng emoji hoặc biểu tượng đặc biệt có liên quan đến bảo mật và quyền riêng tư không.",
    },
    {
        "key": "missing-x-frame-options",
        "value": "thiết lập cài đặt X-Frame-Options đúng cách.",
    },
    {"key": "tech-detect:express", "value": "cập nhật và kiểm tra bảo mật"},
    {
        "key": "display-via-header",
        "value": "Sử dụng các hàm htmlspecialchars() hoặc mysqli_real_escape_string() để lọc dữ liệu đầu vào trước khi hiển thị. Sử dụng prepared statements để thực hiện các truy vấn cơ sở dữ liệu.",
    },
    {"key": "missing-csp", "value": "cấu hình lại chính sách CSP cho ứng dụng web"},
    {"key": "missing-hsts", "value": "bật HSTS trên ứng dụng web."},
    {
        "key": "Express-LFR-GET",
        "value": "đảm bảo rằng ứng dụng của bạn không cho phép người dùng truy cập vào các tệp hệ thống nhạy cảm thông qua yêu cầu GET.",
    },
    {
        "key": "Express-LFR-json",
        "value": "đảm bảo rằng dữ liệu JSON được truyền giữa máy khách và máy chủ được kiểm tra kỹ lưỡng trước khi được thực thi.",
    },
    {
        "key": "possibility-of-webshell",
        "value": "xác định vị trí và loại bỏ webshell khỏi trang web",
    },
    {
        "key": "jira-unauthenticated-user-picker",
        "value": "Sử dụng một bộ lọc để chỉ cho phép người dùng đã xác thực truy cập trang web có chứa chức năng chọn người dùng.Sử dụng một API để thực hiện chức năng chọn người dùng và chỉ cho phép người dùng đã xác thực sử dụng API này.",
    },
    {
        "key": "tongda_sqli2022",
        "value": "Kiểm tra tất cả các truy vấn cơ sở dữ liệu trong ứng dụng của bạn để đảm bảo rằng chúng được bảo vệ khỏi SQL injection.",
    },
    {
        "key": "cors-misconfig:wildcard-no-acac",
        "value": "thêm header Access-Control-Allow-Credentials vào phản hồi của mình.",
    },
]
keys = [i["key"] for i in security_checks]
keys = [i.replace("-", " ") for i in keys]
print(keys)


def jaccard_similarity(set1, set2):
    """
    Calculate Jaccard Similarity between two sets.

    Args:
    set1 (set): The first set of items.
    set2 (set): The second set of items.

    Returns:
    float: Jaccard Similarity score, a value between 0 and 1.
    """
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection

    if union == 0:
        return 0  # Avoid division by zero

    similarity = intersection / union
    return similarity


text = "SSL".replace("-", " ")
set2 = set(text.split(" "))
scores = []
for i in keys:
    set1 = set(i.split(" "))
    similarity_score = jaccard_similarity(set1, set2)
    scores.append((i, similarity_score))
    print("Jaccard Similarity:", similarity_score)


def sort_score(x):
    return x[1]


scores = sorted(scores, key=sort_score)
print(scores)

from cv2 import sort
from transformers import AutoModel, AutoTokenizer
import torch
from scipy.spatial.distance import cosine

# Load a pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def word_embedding_similarity(word1, word2):
    """
    Calculate the similarity between two words using a pre-trained BERT model.

    Args:
    word1 (str): The first word.
    word2 (str): The second word.

    Returns:
    float: The cosine similarity between the word embeddings.
    """
    # Tokenize the words and get their embeddings
    tokens = tokenizer([word1, word2], return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**tokens).last_hidden_state

    # Calculate cosine similarity between the embeddings
    sim_score = 1 - cosine(embeddings[0][0].numpy(), embeddings[1][0].numpy())
    return sim_score

scores = []
for i in keys:
    word1 = "SSL"
    word2 = i
    similarity_score = word_embedding_similarity(word1, word2)
    print(f"BERT Word Embedding Similarity between '{word1}' and '{word2}': {similarity_score:.4f}")
    scores.append([i, similarity_score])

scores = sorted(scores, key=sort_score)
print(scores)