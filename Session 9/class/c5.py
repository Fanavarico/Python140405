alpha = {"salam": "hello", "khodafez": "good bye"}
print(alpha["salam"])
print(alpha["khodafez"])
# print(alpha["how are you"])
# get() -> migarde meqdare marbote be key miare
# age nabod None mide va ya meqdar delkhahe maro mige
print(alpha.get("salam2", 10))