/*
 * dzgram-tgcrypto - Fast and Portable Cryptography Extension Library for Telegram
 * Copyright (C) 2026-present DownloaderZone <https://github.com/DownloaderZone>
 *
 * This file is part of dzgram-tgcrypto.
 *
 * dzgram-tgcrypto is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * dzgram-tgcrypto is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with dzgram-tgcrypto.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef CTR256_H
#define CTR256_H

uint8_t *ctr256(const uint8_t in[], size_t length, const uint8_t key[32], uint8_t iv[16], uint8_t *state);

#endif  // CTR256_H
