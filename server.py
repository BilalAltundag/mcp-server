
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Hesap Makinesi")

@mcp.tool()
def topla(a: float, b: float) -> float:
    """İki sayıyı toplar"""
    return a + b

@mcp.tool()
def cikar(a: float, b: float) -> float:
    """İki sayıyı çıkarır"""
    return a - b

@mcp.tool()
def carp(a: float, b: float) -> float:
    """İki sayıyı çarpar"""
    return a * b

@mcp.tool()
def bol(a: float, b: float) -> float:
    """İki sayıyı böler"""
    if b == 0:
        return "Hata: Sıfıra bölme!"
    return a / b

# HTTP server olarak çalıştır (Render için gerekli)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="sse", port=port, host="0.0.0.0")
