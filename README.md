# 🏆 Student Learning Progress Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Competition](https://img.shields.io/badge/Competition-DataFlow%20Season%202-orange.svg)

**Team:** 4 chị em 412

*An End-to-End Machine Learning Pipeline for Predicting Student Learning Outcomes*

[English](#english) | [Tiếng Việt](#tiếng-việt)

</div>

---

## <a name="english"></a>🇬🇧 English

### 📋 Overview

This project builds an end-to-end machine learning pipeline for predicting student learning progress and outcomes. The solution includes:

- 🔍 Comprehensive Exploratory Data Analysis (EDA)
- ✨ Advanced feature engineering
- 🤖 Ensemble modeling (LightGBM, XGBoost, CatBoost)
- 📊 Interactive dashboard with Explainable AI (SHAP)
- 🎯 Production-ready deployment

### 🎯 Key Features

- **Data Exploration**: In-depth EDA with visualizations and statistical analysis
- **Ensemble Learning**: Combines multiple gradient boosting algorithms for superior predictions
- **Explainability**: SHAP values provide interpretable model insights
- **Interactive Dashboard**: Streamlit-based web interface for result visualization
- **Reproducible Pipeline**: Complete notebook-based training workflow

### 🛠 Prerequisites

**System Requirements:**
- **Operating System:** Windows 10/11, Linux (Ubuntu 20.04+), or MacOS
- **Python:** Version 3.13.5 (or equivalent 3.13.x version)
- **RAM:** Minimum 8GB (16GB recommended for training)
- **Storage:** At least 1GB free space

### ⚙️ Installation

**Step 1:** Clone the repository
```bash
git clone https://github.com/duccminhh-cyber/learning-progress-prediction.git
cd learning-progress-prediction
```

**Step 2:** Install dependencies
```bash
pip install -r requirements.txt
```

> ⏱️ Installation may take a few minutes due to heavy libraries (catboost, shap, streamlit)

### 🚀 Quick Start

> ⚠️ **IMPORTANT:** Always run commands from the project root directory (`learning-progress-prediction`) to avoid path errors.

#### **Step 0: Exploratory Data Analysis (Optional)**

To understand the dataset before training:

1. Open `src/EDA.ipynb` in Jupyter Notebook or VS Code
2. Select the Python kernel with installed dependencies
3. Run all cells sequentially to see:
   - Data distributions and statistics
   - Missing value analysis
   - Feature correlations
   - Visualization of key patterns

#### **Step 1: Train the Model**

1. Open `src/pipeline.ipynb` in Jupyter Notebook or VS Code
2. Select the Python kernel with installed dependencies
3. Run all cells sequentially (Run All)

**Output Files:**
- `model/ensemble_models_grandmaster.pkl` - Trained ensemble model
- `dashboard/dashboard_data.pkl` - Dashboard data (must be in `dashboard/` folder)

#### **Step 2: Generate Predictions**

Predictions on the test set will be automatically saved to `result/submission_final.csv` after completing Step 1.

#### **Step 3: Launch Dashboard**

To run the interactive dashboard:

1. Navigate to the `dashboard` folder where `app.py` is located:
```bash
cd dashboard
```

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Your default browser will automatically open and display the dashboard at: **http://localhost:8501**

> 💡 **Tip:** If the browser doesn't open automatically, manually navigate to the URL shown in the terminal.

### 📂 Project Structure

```
learning-progress-prediction/
├── data/                        # Raw input data
│   ├── academic_records.csv     # Academic history
│   ├── admission.csv            # Admission information
│   └── test.csv                 # Test dataset for predictions
│
├── dashboard/                   # Dashboard application
│   ├── app.py                   # Streamlit dashboard application
│   └── dashboard_data.pkl       # Processed data (SHAP, metrics)
│
├── model/                       # Trained models
│   └── ensemble_models_grandmaster.pkl  # Ensemble model (LGBM + XGB + CatBoost)
│
├── result/                      # Output results
│   └── submission_final.csv     # Final submission file
│
├── src/                         # Source code
│   ├── EDA.ipynb                # Exploratory Data Analysis notebook
│   └── pipeline.ipynb           # Training & evaluation notebook
│
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore configuration
├── LICENSE                      # MIT License
└── README.md                    # This file
```

### 📊 Workflow

```
1. EDA.ipynb           →  Explore & understand the data
2. pipeline.ipynb      →  Train models & generate predictions
3. app.py              →  Visualize results & explain predictions
```

### 🔧 Important Configuration Note

The `dashboard_data.pkl` file is stored in the `dashboard/` folder along with `app.py`. The application automatically loads data from the same directory.


### 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 👥 Team

**Team 4 chị em 412**

Competition: DataFlow Season 2

### 🤝 Contributing

This solution is owned by Team 4 chị em 412. The source code is open for the DataFlow competition organizers for evaluation and non-commercial purposes.

---

## <a name="tiếng-việt"></a>🇻🇳 Tiếng Việt

### 📋 Tổng quan

Dự án xây dựng pipeline End-to-End từ phân tích dữ liệu khám phá (EDA), xử lý dữ liệu, huấn luyện mô hình Ensemble (LightGBM, XGBoost, CatBoost) đến triển khai Dashboard tương tác với Explainable AI (SHAP) để giải thích kết quả dự báo tiến độ và kết quả học tập sinh viên.

### 🎯 Tính năng chính

- **Phân tích dữ liệu khám phá**: EDA chi tiết với trực quan hóa và phân tích thống kê
- **Ensemble Learning**: Kết hợp nhiều thuật toán gradient boosting cho độ chính xác cao
- **Khả năng giải thích**: SHAP values cung cấp cái nhìn chi tiết về mô hình
- **Dashboard tương tác**: Giao diện web Streamlit để hiển thị kết quả
- **Pipeline tái tạo được**: Quy trình huấn luyện đầy đủ bằng notebook

### 🛠 Yêu cầu hệ thống

**Cấu hình tối thiểu:**
- **Hệ điều hành:** Windows 10/11, Linux (Ubuntu 20.04+), hoặc MacOS
- **Python:** Phiên bản 3.13.5 (hoặc phiên bản tương đương 3.13.x)
- **RAM:** Tối thiểu 8GB (Khuyến nghị 16GB để chạy Training Pipeline)
- **Ổ cứng:** Trống tối thiểu 1GB

### ⚙️ Cài đặt

**Bước 1:** Clone repository về máy
```bash
git clone https://github.com/duccminhh-cyber/learning-progress-prediction.git
cd learning-progress-prediction
```

**Bước 2:** Cài đặt các thư viện phụ thuộc
```bash
pip install -r requirements.txt
```

> ⏱️ Quá trình cài đặt có thể mất vài phút do bao gồm các thư viện nặng như catboost, shap, streamlit

### 🚀 Hướng dẫn chạy

> ⚠️ **LƯU Ý QUAN TRỌNG:** Vui lòng luôn mở Terminal tại thư mục gốc (`learning-progress-prediction`) để chạy các lệnh dưới đây. Không cd sâu vào các thư mục con để tránh lỗi đường dẫn.

#### **Bước 0: Phân tích dữ liệu khám phá (Tùy chọn)**

Để hiểu rõ dữ liệu trước khi huấn luyện:

1. Mở file `src/EDA.ipynb` bằng Jupyter Notebook hoặc VS Code
2. Chọn Kernel Python đã cài đặt thư viện
3. Chạy tuần tự các cell để xem:
   - Phân bố và thống kê dữ liệu
   - Phân tích giá trị thiếu
   - Tương quan giữa các đặc trưng
   - Trực quan hóa các mẫu quan trọng

#### **Bước 1: Tiền xử lý & Huấn luyện mô hình**

1. Mở file `src/pipeline.ipynb` bằng Jupyter Notebook hoặc VS Code
2. Chọn Kernel Python đã cài đặt thư viện ở Bước 2
3. Nhấn **Run All** để chạy tuần tự từ trên xuống dưới

**Kết quả sinh ra:**
- `model/ensemble_models_grandmaster.pkl` - Mô hình dự báo
- `dashboard/dashboard_data.pkl` - Dữ liệu cho Dashboard (phải nằm trong thư mục `dashboard/`)

#### **Bước 2: Sinh kết quả dự báo**

Kết quả dự báo trên tập Test sẽ được lưu tự động vào `result/submission_final.csv` sau khi chạy xong Bước 1.

#### **Bước 3: Khởi chạy Dashboard**

Để chạy giao diện Dashboard tương tác:

1. Di chuyển vào thư mục `dashboard` nơi chứa file `app.py`:
```bash
cd dashboard
```

2. Chạy ứng dụng Streamlit:
```bash
streamlit run app.py
```

3. Trình duyệt sẽ tự động mở và hiển thị giao diện Dashboard tại địa chỉ: **http://localhost:8501**

> 💡 **Mẹo:** Nếu trình duyệt không tự động mở, hãy truy cập thủ công vào địa chỉ URL hiển thị trong Terminal.

### 📂 Cấu trúc dự án

```
learning-progress-prediction/
├── data/                        # Chứa dữ liệu đầu vào (Raw Data)
│   ├── academic_records.csv     # Lịch sử học tập
│   ├── admission.csv            # Thông tin tuyển sinh
│   └── test.csv                 # Tập dữ liệu cần dự báo
│
├── dashboard/                   # Ứng dụng Dashboard
│   ├── app.py                   # Giao diện Dashboard (Streamlit)
│   └── dashboard_data.pkl       # File dữ liệu đã xử lý (SHAP, Metrics...)
│
├── model/                       # Chứa Model đã huấn luyện
│   └── ensemble_models_grandmaster.pkl  # Model tổng hợp (LGBM + XGB + CatBoost)
│
├── result/                      # Chứa kết quả đầu ra
│   └── submission_final.csv     # File kết quả nộp bài (Submission)
│
├── src/                         # Mã nguồn chính (Source Code)
│   ├── EDA.ipynb                # Notebook phân tích dữ liệu khám phá
│   └── pipeline.ipynb           # Notebook Training, Feature Eng. & Evaluation
│
├── requirements.txt             # Danh sách các thư viện cần cài đặt
├── .gitignore                   # Cấu hình file ẩn khỏi Git
├── LICENSE                      # Giấy phép mã nguồn
└── README.md                    # Tài liệu hướng dẫn sử dụng (File này)
```

### 📊 Quy trình làm việc

```
1. EDA.ipynb           →  Khám phá & hiểu dữ liệu
2. pipeline.ipynb      →  Huấn luyện mô hình & tạo dự đoán
3. app.py              →  Trực quan hóa kết quả & giải thích dự đoán
```

### 🔧 Lưu ý cấu hình

File `dashboard_data.pkl` được lưu trong thư mục `dashboard/` cùng với `app.py`. Ứng dụng sẽ tự động tải dữ liệu từ cùng thư mục.


### 📝 Bản quyền

Giải pháp thuộc quyền sở hữu của nhóm **4 chị em 412**. Mã nguồn được mở cho BTC DataFlow sử dụng với mục đích chấm thi và phi thương mại.

### 👥 Đội ngũ

**Team 4 chị em 412**

Cuộc thi: DataFlow Season 2

### 🙏 Acknowledgments

- DataFlow Season 2 Competition
- Open-source ML community
- SHAP library for explainability
- Scikit-learn, Pandas, and NumPy communities

---

<div align="center">

**Made with ❤️ by Team 4 chị em 412**

⭐ Star this repo if you find it helpful!

</div>
