
---

## 💸 `pricing.md`

```md
# 💰 SaaS Pricing & Cost Strategy

## 🔖 SaaS Plans (INR Monthly)

| Plan       | Embeddings | Searches/day | Cost      | Margin |
|------------|------------|--------------|-----------|--------|
| Free Tier  | 25K        | 10           | ₹0        | —      |
| Starter    | 100K       | 50           | ₹8,999    | ~55%   |
| Pro        | 1M         | 500          | ₹29,999   | ~63%   |
| Enterprise | Custom     | Custom       | ₹89,999+  | 70%+   |

## 🔄 Usage Metering

- Vector operations tracked in Flask
- Limits based on plan
- Alerts for overage or upgrade trigger

## 📦 Infra Cost Estimates

| Component     | Range (INR/month) |
|---------------|-------------------|
| EC2 Hosting   | ₹4,000–₹5,500     |
| DynamoDB      | ₹400–₹750         |
| ECR + Container | ₹800–₹2,000     |
| CloudWatch    | ₹300–₹600         |

