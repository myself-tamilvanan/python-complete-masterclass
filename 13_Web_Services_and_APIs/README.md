# Chapter 13: Web Services and APIs

## Overview
Web services allow programs to exchange data over the internet. This chapter covers XML, JSON, web APIs, and service-oriented architecture.

## Topics Covered
- XML format and parsing
- JSON format and parsing
- Web APIs and REST
- GeoJSON example
- API Security and rate limiting
- Service Oriented Architecture (SOA)

## Key Concepts
- **XML**: eXtensible Markup Language - hierarchical data format
- **JSON**: JavaScript Object Notation - lightweight data format
- **API**: Application Programming Interface
- **REST**: Representational State Transfer - architectural style
- **Rate Limiting**: Restricting how often you can call an API
- **API Key**: A secret token for authenticating with an API

## Video Timestamps
- 7:23:43 - Using Web Services
- 7:26:35 - XML Format
- 7:37:40 - XML Schema
- 7:51:32 - JSON Format
- 8:03:08 - Service Oriented Approach
- 8:11:33 - GeoJSON Example
- 8:18:49 - API Security & Rate Limiting

## JSON vs XML
| Feature    | JSON            | XML                 |
|------------|-----------------|---------------------|
| Readability | More readable  | More verbose        |
| Size        | Smaller        | Larger              |
| Data types  | Native support | Everything is text  |
| Usage       | Modern APIs    | Older systems       |

## Installation
```bash
pip install requests
```

## Learning Outcomes
- Parse XML and JSON data
- Call web APIs using urllib or requests
- Handle API authentication
- Process structured data from web services