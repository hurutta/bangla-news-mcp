[<img src="https://raw.githubusercontent.com/hurutta/bangla-news-mcp/main/assets/bangla_news_mcp_logo.png" style="height:138px" align="right">](https://github.com/hurutta/bangla-news-mcp)

<div style="display: flex; align-items: center;">

  <div style="flex: 1;">
    <h1 style="margin: 0;">Bangla News MCP Server</h1>
    <p style="margin-top: 0;">A Model Context Protocol (MCP) server that retrieves Bangla news to provide context to LLMs.</p>
  </div>
</div>



<hr>
<div align="center" style="line-height: 0;">

[![MCP](https://badge.mcpx.dev?type=server)](https://github.com/modelcontextprotocol/servers)
[![smithery badge](https://smithery.ai/badge/@hurutta/bangla-news-mcp)](https://smithery.ai/server/@hurutta/bangla-news-mcp)
[![PyPI - Version](https://img.shields.io/pypi/v/bangla-news-mcp)](https://pypi.org/project/bangla-news-mcp/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/tag/hurutta/bangla-news-mcp)](https://img.shields.io/github/v/tag/hurutta/bangla-news-mcp)
[![Issues](https://img.shields.io/github/issues/hurutta/bangla-news-mcp)](https://img.shields.io/github/issues/hurutta/bangla-news-mcp)
[![License](https://img.shields.io/github/license/hurutta/bangla-news-mcp)](https://github.com/hurutta/bangla-news-mcp/blob/main/LICENSE)

</div>


## 📖 Description

A lightweight  [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server delivering bangladeshi news written in bengali language in a structured format. 
Designed for seamless integration with LLM models and news aggregation platforms. 
Fast, scalable, and optimized for bengali language processing.


## 🔬 Installation

### Installing via Smithery

To install bangla-news-mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@hurutta/bangla-news-mcp):

```bash
npx -y @smithery/cli install @hurutta/bangla-news-mcp --client claude
```

### Using a virtual environment
```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the package
pip install git+https://github.com/hurutta/bangla-news-mcp.git
```

### Build from Source
```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Clone the repository
git clone https://github.com/hurutta/bangla-news-mcp
cd bangla-news-mcp

# Install in development mode
pip install -e .
```

## 🔌 Usage


### Configuration for Claude.app
Add to your Claude settings:
```json
{
  "mcpServers": {
    "bangla_news": {
      "command": "python",
      "args": [
        "-m",
        "bangla_news_mcp"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```
👆🏼 If you install pip package inside a virtual environment, adjust the `command` and `args`.

## 🛠️ Available Tools


#### Fetch latest bangla news headlines
 - `fetch_latest_news_headlines`: Returns list of latest bengali news of varied category

#### Fetch bangla news by query
 - `fetch_news_headlines_by_query`: Returns list of bengali news queried by the user


## 🔌 For development

#### Activate the virtual environment where the package is installed, and run -
```bash
source venv/bin/activate
python -m bangla_news_mcp
```

<hr>
