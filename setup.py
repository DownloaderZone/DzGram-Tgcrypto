#  dzgram-tgcrypto - Fast and Portable Cryptography Extension Library for Telegram
#  Copyright (C) 2026-present DownloaderZone <https://github.com/DownloaderZone>
#
#  This file is part of dzgram-tgcrypto.
#
#  dzgram-tgcrypto is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  dzgram-tgcrypto is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with dzgram-tgcrypto.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, Extension, find_packages

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="dzgram-tgcrypto",
    version="1.2.12",
    description="Fast and Portable Cryptography Extension Library for Telegram",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/DownloaderZone/dzgram-tgcrypto",
    download_url="https://github.com/DownloaderZone/dzgram-tgcrypto/releases/latest",
    author="DownloaderZone",
    author_email="DownloaderZone@users.noreply.github.com",
    license="LGPLv3+",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="telegram crypto cryptography encryption mtproto extension library aes",
    project_urls={
        "Source": "https://github.com/DownloaderZone/dzgram-tgcrypto",
        "Tracker": "https://github.com/DownloaderZone/dzgram-tgcrypto/issues",
        "Channel": "https://t.me/DZGramByDzone",
        "Support Group": "https://t.me/DzgramDiscussion",
    },
    python_requires="~=3.7",
    packages=find_packages(exclude=["tests*"]),
    test_suite="tests",
    zip_safe=False,
    ext_modules=[
        Extension(
            "tgcrypto",
            sources=[
                "tgcrypto/tgcrypto.c",
                "tgcrypto/aes256.c",
                "tgcrypto/ige256.c",
                "tgcrypto/ctr256.c",
                "tgcrypto/cbc256.c"
            ]
        )
    ]
)
