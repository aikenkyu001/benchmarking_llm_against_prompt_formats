import λ

def generate_fibonacci(count):
    α = 0
    β = 1
    γ = 0
    for _ in range(count):
        α, β = β, α + β
        γ = α
    return α

---