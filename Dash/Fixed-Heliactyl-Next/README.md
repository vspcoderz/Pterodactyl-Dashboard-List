# Fixed Heliactyl Next • The **most secure & modern** Pterodactyl dashboard

![Last Commit](https://img.shields.io/github/last-commit/OvernodeProjets/fixed-heliactyl-next?color=brightgreen)
![GitHub Release](https://img.shields.io/github/v/release/OvernodeProjets/fixed-heliactyl-next)
![Issues](https://img.shields.io/github/issues/OvernodeProjets/fixed-heliactyl-next)
![License](https://img.shields.io/github/license/OvernodeProjets/fixed-heliactyl-next)
![Dev Branch](https://img.shields.io/badge/status-dev-orange)

> **Dev version only • No stable release yet • Help us build it!**

**Fixed Heliactyl Next** is an **early development fork** of **[Heliactyl Next 3](https://github.com/Heliactyl-Archive/the-library/blob/a9214cda2801ef8effe9db23e26daf5175c62437/README.md?plain=1#L119)**.
It aims to fix critical bugs from older Heliactyl Next 3 versions and improve overall performance and usability.

Currently used by **2–5 hosting providers** in testing — **100% free & open-source**.  
Join us to shape the next stable release!

> [!WARNING]  
> Fixed Heliactyl Next 3 is **not compatible** with `settings.json` old generation files.  
> You can keep the same `database.sqlite` / `heliactyl.db` without issues.

Heliactyl is a high-performance client area for the Pterodactyl Panel. It allows your users to create, edit and delete servers, and earn coins to upgrade their resources.

## Get started

You can get started straight away by following these steps:

1. Clone the repo: Run `git clone https://github.com/OvernodeProjets/fixed-heliactyl-next.git` on your machine
2. Enter the directory and configure the `config_example.toml` file - most are optional except the Pterodactyl API
3. Check everything out and make sure you've configured Heliactyl correctly
4. Create SSL certificates for your target domain and set up the NGINX reverse proxy

## ⚠️ Critical: Configure Pterodactyl Wings

> [!CAUTION]
> **You must configure Wings on every node before deploying Fixed Heliactyl Next!**  
> Without this step, your dashboard will be unable to communicate with Pterodactyl nodes.

For **each node** in your infrastructure, follow these steps:

1. **Locate the Wings configuration file** (typically at `/etc/pterodactyl/config.yml`)
2. **Find the `allowed-origins` setting** in the configuration
3. **Update the value** to one of the following options:

   **Option 1: Allow all origins** (simplest, recommended for testing):
   ```yaml
   allowed-origins: ['*']
   ```

   **Option 2: Restrict to your dashboard domain** (more secure, recommended for production):
   ```yaml
   allowed-origins: ['https://dashboard.yourdomain.com']
   ```

4. **Restart Wings** to apply the changes:
   ```bash
   systemctl restart wings
   ```

## NGINX Reverse Proxy

You can either use a single domain setup or a split domain setup (recommended for production).

### Single Domain Setup
Basic configuration for a single domain:

```nginx
server {
    listen 80;
    server_name <domain>;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name <domain>;

    ssl_certificate /etc/letsencrypt/live/<domain>/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/<domain>/privkey.pem;
    ssl_session_cache shared:SSL:10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # WebSocket support for AFK system
    location /api/afk/ws {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass "http://localhost:<port>/api/afk/ws";
    }

    # WebSocket support for server stats (real-time monitoring)
    location ~ ^/api/server/[^/]+/ws$ {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
        proxy_pass http://localhost:<port>;
    }

    location / {
        proxy_pass http://localhost:<port>/;
        proxy_buffering off;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Split Domain Setup (Recommended)
For a production environment, we recommend splitting your website and dashboard into separate domains:

1. Main website configuration (e.g., yourdomain.com):
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_session_cache shared:SSL:10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Redirect dashboard routes to dashboard domain
    location /auth {
        return 301 https://dashboard.yourdomain.com/auth;
    }
    
    location /dashboard {
        return 301 https://dashboard.yourdomain.com/dashboard;
    }

    # Serve only homepage and static assets
    location / {
        proxy_pass http://localhost:<port>/website;
        proxy_buffering off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Website-Only "true";
    }

    location /assets {
        proxy_pass http://localhost:<port>/assets;
        proxy_buffering off;
    }
}
```

2. Dashboard configuration (e.g., dashboard.yourdomain.com):
```nginx
server {
    listen 80;
    server_name dashboard.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name dashboard.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/dashboard.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/dashboard.yourdomain.com/privkey.pem;
    ssl_session_cache shared:SSL:10m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # WebSocket support for AFK system
    location /api/afk/ws {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass "http://localhost:<port>/api/afk/ws";
    }

    # WebSocket support for server stats (real-time monitoring)
    location ~ ^/api/server/[^/]+/ws$ {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
        proxy_pass http://localhost:<port>;
    }

    # Redirect root to auth page
    location = / {
        return 301 https://dashboard.yourdomain.com/auth;
    }

    # Block access to website page on dashboard domain
    location /website {
        return 404;
    }

    location / {
        proxy_pass http://localhost:<port>;
        proxy_buffering off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Dashboard-Only "true";
    }
}
```

3. Update your config.toml:
```toml
[website]
port = 3000
domain = "https://dashboard.yourdomain.com"  # Dashboard domain
```

Make sure to:
1. Replace <port> with your Heliactyl port (default: 3000)
2. Replace yourdomain.com with your actual domain
3. Generate SSL certificates for both domains
4. Create separate nginx config files for each domain
5. Enable the configurations and restart nginx

## Development Tools

These commands are available:
```
npm run start - starts Heliactyl
npm run build:css - builds TailwindCSS, required for making changes to the UI
```


## Troubleshooting

### Velocity Proxy Issues
If you encounter version or installation issues with Velocity (e.g., "latest" version not found), please update your Egg configuration using the fixed JSON file available here:
[Fixed Velocity Egg](https://github.com/OvernodeProjets/minecraft-eggs/blob/main/proxy/java/velocity/egg-pterodactyl-velocity.json)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
Copyright (c) 2017 - 2025 Foundry Technologies Inc
Copyright (c) 2022 - 2025 Overnode
```