# Chapter 12: Networked Programs
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

import socket
import urllib.parse
import urllib.request

# -----------------------------------------------
# SECTION 1: Simple Socket Connection
# -----------------------------------------------

print("--- Socket Connection ---")

# Sockets are the lowest-level networking in Python
# This is similar to writing a basic web browser


def fetch_with_socket(host, path="/"):
    """Fetch a web page using raw sockets."""
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))  # Port 80 for HTTP

    # HTTP request format: GET /path HTTP/1.0
    cmd = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
    mysock.send(cmd.encode())  # Must send bytes, not string

    data = b""
    while True:
        chunk = mysock.recv(512)
        if not chunk:
            break
        data += chunk

    mysock.close()
    return data.decode(errors="replace")


# Example usage (uncomment to run):
# content = fetch_with_socket("data.pr4e.org", "/romeo.txt")
# print(content[:500])

print("Socket example defined (uncomment to fetch)")

# -----------------------------------------------
# SECTION 2: Using urllib (Simpler Approach)
# -----------------------------------------------

print("\n--- urllib ---")


def fetch_url(url):
    """Fetch content from a URL using urllib."""
    try:
        fhand = urllib.request.urlopen(url)
        content = fhand.read().decode()
        fhand.close()
        return content
    except Exception as e:
        return f"Error: {e}"


# Fetch a simple text file
url = "http://data.pr4e.org/romeo.txt"
# content = fetch_url(url)
# print("First 200 chars:", content[:200])
print("urllib fetch function defined")

# -----------------------------------------------
# SECTION 3: Counting Words from Web
# -----------------------------------------------

print("\n--- Word Count from URL ---")


def count_words_from_url(url):
    """Count word frequencies from a URL."""
    try:
        fhand = urllib.request.urlopen(url)
        counts = {}
        for line in fhand:
            words = line.decode().split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
        fhand.close()
        return counts
    except Exception:
        return {}


# Uncomment to run:
# counts = count_words_from_url("http://data.pr4e.org/romeo.txt")
# sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# print("Top 10 words:")
# for word, count in sorted_counts[:10]:
#     print(f"  {word}: {count}")

# -----------------------------------------------
# SECTION 4: HTML Parsing with BeautifulSoup
# -----------------------------------------------

print("\n--- HTML Parsing ---")

# Install: pip install beautifulsoup4
# from urllib.request import urlopen
# from bs4 import BeautifulSoup


def extract_links(url):
    """Extract all links from a web page."""
    # Requires: pip install beautifulsoup4
    try:
        from bs4 import BeautifulSoup

        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        links = []
        for tag in soup("a"):
            href = tag.get("href", None)
            if href:
                links.append(href)
        return links
    except ImportError:
        return ["BeautifulSoup not installed. Run: pip install beautifulsoup4"]
    except Exception as e:
        return [f"Error: {e}"]


# Example usage:
# links = extract_links("http://www.dr-chuck.com/page1.htm")
# for link in links:
#     print(link)

# -----------------------------------------------
# SECTION 5: Unicode and Character Encoding
# -----------------------------------------------

print("\n--- Unicode and UTF-8 ---")

# Python 3 strings are Unicode by default
unicode_str = "Hello World"
print("String:", unicode_str)
print("Type:", type(unicode_str))

# Encode to bytes
encoded = unicode_str.encode("utf-8")
print("Encoded (bytes):", encoded)
print("Type:", type(encoded))

# Decode back to string
decoded = encoded.decode("utf-8")
print("Decoded:", decoded)

# Unicode characters
emoji = "Python \u2764"  # Heart character
print("Unicode:", emoji)

print("\n" + "=" * 50)
print("Chapter 12 Complete!")
print("=" * 50)
