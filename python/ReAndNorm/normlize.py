from unicodedata import normalize
import re


#[̀-ͯ]
message = re.sub(
        #[in squre bracket it is charater class] (group of regex)
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize("NFD", "Hello"), 0, re.I
    )

print(message)
print(normalize("NFD","[\u0300-\u036f]"))
print(normalize("NFD","[^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]"))
