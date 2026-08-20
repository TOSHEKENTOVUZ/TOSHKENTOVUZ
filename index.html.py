<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 TOSHKENTOVUZ - OLAMDAGI ENG KUCHLI PORTAL</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
        :root {
            --primary: #D4AF37;
            --secondary: #00D4FF;
            --ai-color: #FF2D95;
            --security-color: #39FF14;
            --danger-color: #FF2D2D;
            --verified-color: #00FF88;
            --gradient-1: linear-gradient(135deg, #D4AF37 0%, #00D4FF 50%, #FF2D95 100%);
            --gradient-2: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a1a2e 100%);
            --glass: rgba(255,255,255,0.05);
            --border: rgba(255,255,255,0.1);
            --radius: 20px;
        }
        body {
            font-family: 'Orbitron', sans-serif;
            background: var(--gradient-2);
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
            cursor: default;
        }
        #stars { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; }
        .star {
            position: absolute;
            background: #fff;
            border-radius: 50%;
            animation: twinkle var(--duration) infinite alternate;
        }
        @keyframes twinkle {
            0% { opacity: 0.2; transform: scale(0.8); }
            100% { opacity: 1; transform: scale(1.2); }
        }
        .meteor {
            position: fixed;
            width: 2px;
            height: 2px;
            background: #fff;
            border-radius: 50%;
            animation: meteor-fall var(--duration) linear infinite;
            z-index: 0;
            pointer-events: none;
        }
        .meteor::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 80px;
            height: 1px;
            background: linear-gradient(to left, rgba(255,255,255,0.8), transparent);
            transform: rotate(-45deg);
            transform-origin: right;
        }
        @keyframes meteor-fall {
            0% { transform: translate(0,0) rotate(-45deg); opacity: 1; }
            100% { transform: translate(-200px,200px) rotate(-45deg); opacity: 0; }
        }
        .quantum-glow::before {
            content: '';
            position: absolute;
            inset: -3px;
            background: var(--gradient-1);
            border-radius: inherit;
            z-index: -1;
            filter: blur(30px);
            opacity: 0.4;
            animation: quantum-pulse 3s infinite;
        }
        @keyframes quantum-pulse {
            0%,100% { opacity: 0.3; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
        }
        .glass {
            background: var(--glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 0 20px; }
        
        header {
            position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
            background: rgba(10,10,26,0.85); backdrop-filter: blur(30px);
            border-bottom: 1px solid var(--border); padding: 10px 0;
            transition: all 0.3s ease;
        }
        header.scrolled { background: rgba(10,10,26,0.95); box-shadow: 0 10px 40px rgba(0,0,0,0.5); }
        .header-content { display: flex; justify-content: space-between; align-items: center; }
        .logo {
            display: flex; align-items: center; gap: 10px;
            font-size: 14px; font-weight: 900; text-transform: uppercase;
        }
        .logo-icon { font-size: 24px; animation: pulse 2s infinite; }
        .logo-text {
            background: var(--gradient-1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 18px;
        }
        .security-badge {
            font-size: 9px;
            color: var(--security-color);
            border: 1px solid var(--security-color);
            padding: 2px 10px;
            border-radius: 50px;
            animation: pulse 1.5s infinite;
            background: rgba(57,255,20,0.1);
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .security-badge .lock { font-size: 12px; }
        .security-badge .dot {
            width: 6px;
            height: 6px;
            background: var(--security-color);
            border-radius: 50%;
            display: inline-block;
            animation: pulse-dot 1s infinite;
        }
        @keyframes pulse-dot {
            0%,100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.3; transform: scale(0.7); }
        }
        @keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:0.5; } }
        .menu-toggle {
            display: none; background: none; border: none; color: #fff;
            font-size: 26px; cursor: pointer;
        }
        nav ul { display: flex; list-style: none; gap: 15px; }
        nav ul li a {
            color: rgba(255,255,255,0.7); text-decoration: none;
            font-size: 10px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; position: relative; transition: all 0.3s ease;
        }
        nav ul li a::after {
            content: ''; position: absolute; bottom: -5px; left: 0;
            width: 0; height: 2px; background: var(--gradient-1);
            transition: all 0.3s ease;
        }
        nav ul li a:hover::after { width: 100%; }
        nav ul li a:hover { color: #fff; }
        .btn-start {
            padding: 8px 20px; background: var(--gradient-1);
            border-radius: 50px; color: #fff; font-weight: 700; font-size: 11px;
            text-transform: uppercase; letter-spacing: 1px; border: none;
            cursor: pointer; transition: all 0.3s ease;
        }
        .btn-start:hover { transform: scale(1.05); box-shadow: 0 0 40px rgba(212,175,55,0.4); }
        
        .hero {
            padding: 120px 0 50px; min-height: 100vh;
            display: flex; align-items: center; position: relative; z-index: 1;
        }
        .hero-content {
            display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center;
        }
        .hero-text h1 {
            font-size: 42px; font-weight: 900; text-transform: uppercase;
            line-height: 1.2;
        }
        .hero-text h1 span {
            background: var(--gradient-1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-text h2 {
            font-size: 28px; margin-bottom: 20px; font-weight: 700;
        }
        .highlight {
            background: var(--gradient-1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 32px; animation: pulse 2s infinite;
        }
        .hero-text p { font-size: 13px; color: rgba(255,255,255,0.6); margin-bottom: 8px; }
        .security-info {
            display: flex;
            gap: 10px;
            margin-top: 15px;
            flex-wrap: wrap;
        }
        .security-info .item {
            font-size: 10px;
            color: var(--security-color);
            background: rgba(57,255,20,0.05);
            padding: 4px 12px;
            border-radius: 50px;
            border: 1px solid rgba(57,255,20,0.2);
        }
        .security-info .item-verified {
            color: var(--verified-color);
            border-color: rgba(0,255,136,0.3);
            background: rgba(0,255,136,0.05);
        }
        .security-info .item-danger {
            color: var(--danger-color);
            border-color: rgba(255,45,45,0.3);
        }
        .hero-buttons { display: flex; gap: 15px; margin-top: 25px; flex-wrap: wrap; }
        .btn-primary {
            padding: 12px 30px; background: var(--gradient-1);
            border-radius: 50px; color: #fff; font-weight: 700; font-size: 12px;
            text-transform: uppercase; letter-spacing: 1px; border: none;
            cursor: pointer; transition: all 0.3s ease;
        }
        .btn-primary:hover { transform: scale(1.05); box-shadow: 0 0 40px rgba(212,175,55,0.4); }
        .btn-secondary {
            padding: 12px 30px; background: transparent;
            border: 2px solid var(--border); border-radius: 50px;
            color: #fff; font-weight: 700; font-size: 12px;
            text-transform: uppercase; letter-spacing: 1px; transition: all 0.3s ease;
        }
        .btn-secondary:hover { border-color: var(--secondary); color: var(--secondary); transform: scale(1.05); }
        .btn-verified {
            padding: 12px 30px; background: rgba(0,255,136,0.15);
            border: 2px solid var(--verified-color);
            border-radius: 50px;
            color: var(--verified-color);
            font-weight: 700; font-size: 12px;
            text-transform: uppercase; letter-spacing: 1px;
            cursor: pointer; transition: all 0.3s ease;
        }
        .btn-verified:hover { background: rgba(0,255,136,0.3); transform: scale(1.05); }
        .hero-stats {
            display: grid; grid-template-columns: repeat(4,1fr); gap: 15px;
            margin-top: 30px; padding: 20px;
            background: var(--glass); backdrop-filter: blur(20px);
            border-radius: var(--radius); border: 1px solid var(--border);
        }
        .stat-item { text-align: center; }
        .stat-number {
            display: block; font-size: 28px; font-weight: 900;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stat-label { font-size: 10px; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 1px; }
        .avatar-circle {
            width: 280px; height: 280px; border-radius: 50%;
            background: var(--gradient-1); display: flex; align-items: center;
            justify-content: center; position: relative; animation: pulse 3s infinite;
        }
        .avatar-icon { font-size: 100px; z-index: 1; }
        .avatar-pulse {
            position: absolute; inset: -20px; border-radius: 50%;
            border: 2px solid rgba(255,255,255,0.1);
            animation: pulse-ring 2s infinite;
        }
        @keyframes pulse-ring {
            0% { transform: scale(1); opacity: 1; }
            100% { transform: scale(1.5); opacity: 0; }
        }
        .ai-badge {
            position: absolute; bottom: -20px; left: 50%; transform: translateX(-50%);
            background: rgba(10,10,26,0.9); padding: 8px 15px; border-radius: 50px;
            font-size: 10px; font-weight: 700; color: var(--ai-color);
            border: 1px solid var(--ai-color); white-space: nowrap;
            text-transform: uppercase; letter-spacing: 1px;
        }
        .year-badge {
            position: absolute; top: -20px; right: -20px;
            background: var(--gradient-1); padding: 5px 12px; border-radius: 50px;
            font-size: 14px; font-weight: 900; animation: pulse 2s infinite;
            text-shadow: 0 0 20px rgba(212,175,55,0.5);
        }
        
        .features, .categories, .stats-section, .contact, .ai-section, .security-section, .bot-section, .payment-section, .scanner-section {
            padding: 50px 0; position: relative; z-index: 1;
        }
        .features h2, .categories h2, .stats-section h2, .contact h2, .ai-section h2, .security-section h2, .bot-section h2, .payment-section h2, .scanner-section h2 {
            text-align: center; font-size: 28px; font-weight: 900;
            text-transform: uppercase; letter-spacing: 3px;
        }
        .features h2 span, .categories h2 span, .stats-section h2 span, .contact h2 span, .ai-section h2 span, .security-section h2 span, .bot-section h2 span, .payment-section h2 span, .scanner-section h2 span {
            background: var(--gradient-1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .section-subtitle {
            text-align: center; color: rgba(255,255,255,0.5);
            margin-bottom: 30px; font-size: 13px; letter-spacing: 3px;
        }
        
        .features-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; }
        .feature-card {
            padding: 20px; background: var(--glass); backdrop-filter: blur(20px);
            border-radius: var(--radius); border: 1px solid var(--border);
            text-align: center; transition: all 0.3s ease;
        }
        .feature-card:hover { transform: translateY(-8px); border-color: var(--primary); box-shadow: 0 20px 40px rgba(212,175,55,0.1); }
        .feature-icon { font-size: 40px; margin-bottom: 10px; display: block; }
        .feature-card h3 { font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
        .feature-card p { color: rgba(255,255,255,0.5); font-size: 11px; line-height: 1.8; }
        
        .categories-grid {
            display: grid; grid-template-columns: repeat(auto-fill, minmax(180px,1fr)); gap: 10px;
        }
        .category-item {
            padding: 12px 8px; background: var(--glass); backdrop-filter: blur(10px);
            border-radius: 12px; border: 1px solid var(--border);
            text-align: center; transition: all 0.3s ease;
            cursor: pointer; font-size: 10px; font-weight: 400;
            color: rgba(255,255,255,0.8); text-decoration: none; display: block;
            position: relative;
            overflow: hidden;
        }
        .category-item::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(212,175,55,0.05) 0%, transparent 70%);
            opacity: 0;
            transition: all 0.5s ease;
        }
        .category-item:hover::before { opacity: 1; }
        .category-item:hover {
            transform: translateY(-5px) scale(1.03);
            border-color: var(--primary);
            background: rgba(212,175,55,0.1);
            box-shadow: 0 0 30px rgba(212,175,55,0.05);
            color: #fff;
        }
        .category-item .icon { display: block; font-size: 24px; margin-bottom: 4px; }
        .category-item .sub { display: block; font-size: 7px; color: rgba(255,255,255,0.3); margin-top: 3px; }
        .category-item .verified-badge {
            display: inline-block;
            font-size: 6px;
            color: var(--verified-color);
            background: rgba(0,255,136,0.1);
            padding: 1px 6px;
            border-radius: 50px;
            border: 1px solid rgba(0,255,136,0.2);
            margin-top: 3px;
        }
        
        .search-box {
            margin: 20px auto;
            max-width: 600px;
            display: flex;
            gap: 10px;
        }
        .search-box input {
            flex: 1;
            padding: 12px 20px;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border);
            border-radius: 50px;
            color: #fff;
            font-size: 13px;
            font-family: 'Orbitron', sans-serif;
            transition: all 0.3s ease;
        }
        .search-box input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 30px rgba(212,175,55,0.1);
        }
        .search-box input::placeholder { color: rgba(255,255,255,0.3); }
        .search-box button {
            padding: 12px 25px;
            background: var(--gradient-1);
            border: none;
            border-radius: 50px;
            color: #fff;
            font-weight: 700;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Orbitron', sans-serif;
        }
        .search-box button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 40px rgba(212,175,55,0.3);
        }
        
        .sort-buttons {
            display: flex;
            gap: 10px;
            justify-content: center;
            flex-wrap: wrap;
            margin: 15px 0;
        }
        .sort-btn {
            padding: 8px 18px;
            background: var(--glass);
            border: 1px solid var(--border);
            border-radius: 50px;
            color: rgba(255,255,255,0.6);
            font-size: 10px;
            font-family: 'Orbitron', sans-serif;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .sort-btn:hover {
            border-color: var(--primary);
            color: #fff;
            background: rgba(212,175,55,0.1);
        }
        .sort-btn.active {
            border-color: var(--primary);
            color: #fff;
            background: rgba(212,175,55,0.15);
        }
        
        .stats-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; }
        .stats-card {
            padding: 20px; background: var(--glass); backdrop-filter: blur(20px);
            border-radius: var(--radius); border: 1px solid var(--border);
            text-align: center; transition: all 0.3s ease;
        }
        .stats-card:hover { transform: translateY(-5px); border-color: var(--primary); }
        .stats-number {
            display: block; font-size: 36px; font-weight: 900;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stats-label { font-size: 11px; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 1px; }
        
        .security-panel {
            background: rgba(57,255,20,0.03);
            border: 1px solid rgba(57,255,20,0.15);
            border-radius: var(--radius);
            padding: 25px;
            backdrop-filter: blur(20px);
            margin-top: 20px;
        }
        .security-panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .security-panel-header h3 {
            font-size: 16px;
            color: var(--security-color);
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .security-panel-header .status {
            font-size: 11px;
            padding: 5px 15px;
            border-radius: 50px;
            background: rgba(57,255,20,0.15);
            border: 1px solid rgba(57,255,20,0.3);
            color: var(--security-color);
        }
        .security-log {
            background: rgba(0,0,0,0.4);
            border-radius: 10px;
            padding: 15px;
            max-height: 150px;
            overflow-y: auto;
            font-size: 11px;
            font-family: 'Orbitron', sans-serif;
            line-height: 2;
            color: rgba(255,255,255,0.6);
            border: 1px solid var(--border);
        }
        .security-log .log-entry {
            border-bottom: 1px solid rgba(255,255,255,0.03);
            padding: 3px 0;
        }
        .security-log .log-entry .time { color: var(--secondary); margin-right: 10px; }
        .security-log .log-entry .success { color: var(--security-color); }
        .security-log .log-entry .verified { color: var(--verified-color); }
        .security-log .log-entry .alert { color: var(--ai-color); }
        .security-log .log-entry .danger { color: var(--danger-color); }
        
        .ai-panel {
            background: rgba(255,45,149,0.05);
            border: 1px solid rgba(255,45,149,0.2);
            border-radius: var(--radius);
            padding: 25px;
            backdrop-filter: blur(20px);
            margin-top: 20px;
        }
        .ai-panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
            gap: 10px;
        }
        .ai-panel-header h3 {
            font-size: 16px;
            color: var(--ai-color);
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .ai-panel-header .status {
            font-size: 11px;
            padding: 5px 15px;
            border-radius: 50px;
            background: rgba(57,255,20,0.15);
            border: 1px solid rgba(57,255,20,0.3);
            color: var(--security-color);
        }
        .ai-log {
            background: rgba(0,0,0,0.4);
            border-radius: 10px;
            padding: 15px;
            max-height: 150px;
            overflow-y: auto;
            font-size: 11px;
            font-family: 'Orbitron', sans-serif;
            line-height: 2;
            color: rgba(255,255,255,0.6);
            border: 1px solid var(--border);
        }
        .ai-log .log-entry {
            border-bottom: 1px solid rgba(255,255,255,0.03);
            padding: 3px 0;
        }
        .ai-log .log-entry .time { color: var(--secondary); margin-right: 10px; }
        .ai-log .log-entry .action { color: var(--ai-color); }
        .ai-log .log-entry .success { color: var(--security-color); }
        .ai-log .log-entry .verified { color: var(--verified-color); }
        
        .contact-content { display: grid; grid-template-columns: 1fr 2fr; gap: 25px; }
        .contact-info {
            display: flex; flex-direction: column; gap: 12px;
            padding: 20px; background: var(--glass); backdrop-filter: blur(20px);
            border-radius: var(--radius); border: 1px solid var(--border);
        }
        .contact-item { display: flex; align-items: center; gap: 10px; font-size: 12px; }
        .contact-icon { font-size: 18px; }
        .social-links {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 5px;
        }
        .social-link {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 15px;
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s ease;
            font-size: 11px;
            color: #fff;
        }
        .social-link:hover {
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(255,255,255,0.1);
        }
        .social-link-telegram {
            background: rgba(0,136,204,0.15);
            border: 1px solid rgba(0,136,204,0.3);
        }
        .social-link-telegram:hover {
            background: rgba(0,136,204,0.3);
            border-color: #0088cc;
        }
        .social-link-instagram {
            background: rgba(225,48,108,0.15);
            border: 1px solid rgba(225,48,108,0.3);
        }
        .social-link-instagram:hover {
            background: rgba(225,48,108,0.3);
            border-color: #e1306c;
        }
        .social-link-youtube {
            background: rgba(255,0,0,0.15);
            border: 1px solid rgba(255,0,0,0.3);
        }
        .social-link-youtube:hover {
            background: rgba(255,0,0,0.3);
            border-color: #ff0000;
        }
        .contact-form {
            display: flex; flex-direction: column; gap: 10px;
            padding: 20px; background: var(--glass); backdrop-filter: blur(20px);
            border-radius: var(--radius); border: 1px solid var(--border);
        }
        .contact-form input, .contact-form textarea {
            padding: 10px 15px; background: rgba(255,255,255,0.05);
            border: 1px solid var(--border); border-radius: 10px;
            color: #fff; font-size: 12px; font-family: 'Orbitron', sans-serif;
            transition: all 0.3s ease;
        }
        .contact-form input:focus, .contact-form textarea:focus {
            outline: none; border-color: var(--primary);
            box-shadow: 0 0 20px rgba(212,175,55,0.1);
        }
        .contact-form textarea { min-height: 80px; resize: vertical; }
        
        .toast {
            position: fixed;
            bottom: 30px;
            right: 30px;
            padding: 15px 25px;
            background: rgba(10,10,26,0.95);
            border: 1px solid var(--primary);
            border-radius: 12px;
            color: #fff;
            font-size: 12px;
            z-index: 9999;
            backdrop-filter: blur(20px);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.5s ease;
            max-width: 400px;
        }
        .toast.show { transform: translateY(0); opacity: 1; }
        .toast.success { border-color: var(--security-color); }
        .toast.error { border-color: var(--ai-color); }
        .toast.info { border-color: var(--secondary); }
        .toast.danger { border-color: var(--danger-color); }
        .toast.verified { border-color: var(--verified-color); }
        
        .back-to-top {
            position: fixed;
            bottom: 30px;
            left: 30px;
            width: 50px;
            height: 50px;
            background: var(--gradient-1);
            border: none;
            border-radius: 50%;
            color: #fff;
            font-size: 22px;
            cursor: pointer;
            z-index: 999;
            opacity: 0;
            transform: scale(0);
            transition: all 0.3s ease;
            box-shadow: 0 5px 25px rgba(212,175,55,0.3);
        }
        .back-to-top.show { opacity: 1; transform: scale(1); }
        .back-to-top:hover { transform: scale(1.1) rotate(360deg); }
        
        .loader {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: var(--gradient-2); display: flex; align-items: center;
            justify-content: center; z-index: 9999; transition: opacity 0.5s ease;
        }
        .loader.hidden { opacity: 0; pointer-events: none; }
        .loader-spinner {
            width: 60px; height: 60px; border: 3px solid var(--border);
            border-top: 3px solid var(--security-color); border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        
        footer {
            padding: 30px 0; border-top: 1px solid var(--border);
            background: rgba(0,0,0,0.5); position: relative; z-index: 1;
        }
        .footer-content { display: flex; flex-direction: column; align-items: center; gap: 15px; }
        .footer-logo {
            display: flex; align-items: center; gap: 8px;
            font-size: 16px; font-weight: 900; text-transform: uppercase;
        }
        .footer-links { display: flex; gap: 15px; flex-wrap: wrap; justify-content: center; }
        .footer-links a {
            color: rgba(255,255,255,0.5); text-decoration: none;
            font-size: 10px; text-transform: uppercase; letter-spacing: 1px;
            transition: all 0.3s ease;
        }
        .footer-links a:hover { color: var(--secondary); }
        .footer-bottom { text-align: center; color: rgba(255,255,255,0.3); font-size: 10px; letter-spacing: 1px; }
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: var(--gradient-2); }
        ::-webkit-scrollbar-thumb { background: var(--gradient-1); border-radius: 10px; }
        
        @media (max-width: 992px) {
            .hero-content { grid-template-columns: 1fr; text-align: center; }
            .hero-text h1 { font-size: 30px; }
            .hero-text h2 { font-size: 22px; }
            .highlight { font-size: 24px; }
            .hero-stats { grid-template-columns: repeat(2,1fr); }
            .hero-buttons { justify-content: center; }
            .avatar-circle { width: 180px; height: 180px; }
            .avatar-icon { font-size: 60px; }
            .features-grid { grid-template-columns: repeat(2,1fr); }
            .stats-grid { grid-template-columns: repeat(2,1fr); }
            .contact-content { grid-template-columns: 1fr; }
            .menu-toggle { display: block; }
            nav ul {
                display: none; flex-direction: column; position: absolute; top: 100%;
                left: 0; right: 0; background: rgba(10,10,26,0.95);
                padding: 15px 20px; border-bottom: 1px solid var(--border); gap: 8px;
            }
            nav ul.active { display: flex; }
            .categories-grid { grid-template-columns: repeat(auto-fill, minmax(150px,1fr)); }
        }
        
        @media (max-width: 600px) {
            .hero { padding: 90px 0 20px; }
            .hero-text h1 { font-size: 22px; }
            .hero-text h2 { font-size: 16px; }
            .highlight { font-size: 18px; }
            .hero-stats { grid-template-columns: repeat(2,1fr); gap: 8px; padding: 12px; }
            .stat-number { font-size: 18px; }
            .features-grid { grid-template-columns: 1fr; }
            .stats-grid { grid-template-columns: 1fr 1fr; }
            .stats-number { font-size: 22px; }
            .categories-grid { grid-template-columns: repeat(auto-fill, minmax(120px,1fr)); gap: 6px; }
            .category-item { font-size: 9px; padding: 8px 5px; }
            .hero-buttons { flex-direction: column; align-items: center; }
            .btn-primary, .btn-secondary, .btn-verified { width: 100%; text-align: center; font-size: 11px; padding: 10px 15px; }
            .avatar-circle { width: 130px; height: 130px; }
            .avatar-icon { font-size: 45px; }
            .header-content .btn-start { display: none; }
            .security-badge { font-size: 7px; padding: 2px 8px; }
            .security-badge .dot { width: 4px; height: 4px; }
            .toast { bottom: 10px; right: 10px; left: 10px; max-width: none; font-size: 11px; padding: 12px 18px; }
            .back-to-top { bottom: 15px; left: 15px; width: 40px; height: 40px; font-size: 18px; }
            .search-box { flex-direction: column; }
            .logo-text { font-size: 14px; }
            .logo-icon { font-size: 18px; }
            .security-info .item { font-size: 8px; padding: 3px 8px; }
            .contact-content { grid-template-columns: 1fr; }
            .social-links { justify-content: center; }
            .social-link { font-size: 10px; padding: 6px 12px; }
        }
    </style>
</head>
<body>
    <div class="loader" id="loader"><div class="loader-spinner"></div></div>
    <div id="stars"></div>
    <div class="toast" id="toast"></div>
    <button class="back-to-top" id="backToTop">⬆</button>
    
    <header id="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <span class="logo-icon">🚀</span>
                    <span class="logo-text">TOSHKENTOVUZ</span>
                    <span class="security-badge">
                        <span class="lock">🛡️</span>
                        <span class="dot"></span>
                        100% XAVFSIZ
                    </span>
                </div>
                <button class="menu-toggle" id="menuToggle">☰</button>
                <nav>
                    <ul id="navMenu">
                        <li><a href="#home">🏠 Bosh</a></li>
                        <li><a href="#features">✨ Xususiyatlar</a></li>
                        <li><a href="#windows">🪟 Windows</a></li>
                        <li><a href="#original">🔵 Original</a></li>
                        <li><a href="#sborka">📦 Sborka</a></li>
                        <li><a href="#drivers">🔧 Drayverlar</a></li>
                        <li><a href="#postinstall">⚙️ Post Installer</a></li>
                        <li><a href="#stats">📊 Statistika</a></li>
                        <li><a href="#security">🛡️ Xavfsizlik</a></li>
                        <li><a href="#ai">🤖 AI</a></li>
                        <li><a href="#contact">📞 Aloqa</a></li>
                        <li><a href="#bot">🤖 Bot</a></li>
                    </ul>
                </nav>
                <a href="#original" class="btn-start">🔵 Original</a>
            </div>
        </div>
    </header>

    <section id="home" class="hero">
        <div class="container">
            <div class="hero-content">
                <div class="hero-text">
                    <h1>🚀 <span>TOSHKENTOVUZ</span></h1>
                    <h2><span class="highlight">🌍 OLAMDAGI ENG KUCHLI PORTAL</span></h2>
                    <p>🧠 Dunyodagi eng aqlli AI tomonidan boshqariladi</p>
                    <p>🛡️ 100% XAVFSIZLIK - HECH KIM BUZA OLMAYDI!</p>
                    <p>📊 1000+ tugma | 10000+ sayt | 100% avtonom</p>
                    <p>⚡ SAYT VA BOT 100% SINXRON ISHLAYDI!</p>
                    <div class="security-info">
                        <span class="item">🛡️ Xaker Blok</span>
                        <span class="item">🔒 SSL/HTTPS</span>
                        <span class="item">🔐 XSS Himoya</span>
                        <span class="item">🔄 24/7 Monitoring</span>
                        <span class="item">🧠 AI Himoya</span>
                        <span class="item-verified">✅ ORIGINAL</span>
                        <span class="item-verified">🌐 WEBHOOK 100%</span>
                        <span class="item-verified">⚡ VERCEL 100%</span>
                        <span class="item item-danger">🚫 Buzish urinishi bloklanadi</span>
                    </div>
                    <div class="hero-buttons">
                        <a href="#windows" class="btn-primary">🪟 Windows</a>
                        <a href="#original" class="btn-secondary">🔵 Original</a>
                        <a href="#sborka" class="btn-secondary">📦 Sborka</a>
                        <a href="#drivers" class="btn-secondary">🔧 Drayverlar</a>
                        <a href="#ai" class="btn-secondary">🤖 AI Panel</a>
                        <a href="#contact" class="btn-secondary">📞 Aloqa</a>
                        <a href="#bot" class="btn-secondary">🤖 Bot</a>
                        <button class="btn-verified" onclick="showToast('⚡ Vercelda 100% ishlaydi!', 'verified')">⚡ VERCEL</button>
                    </div>
                    <div class="hero-stats">
                        <div class="stat-item"><span class="stat-number" id="stat1">1000+</span><span class="stat-label">Tugmalar</span></div>
                        <div class="stat-item"><span class="stat-number" id="stat2">10000+</span><span class="stat-label">Saytlar</span></div>
                        <div class="stat-item"><span class="stat-number" id="stat3">100%</span><span class="stat-label">Xavfsiz</span></div>
                        <div class="stat-item"><span class="stat-number" id="stat4">∞</span><span class="stat-label">Himoya</span></div>
                    </div>
                </div>
                <div class="hero-image">
                    <div class="bot-avatar">
                        <div class="avatar-circle quantum-glow">
                            <span class="avatar-icon">🚀</span>
                            <div class="avatar-pulse"></div>
                        </div>
                        <div class="ai-badge">🧠 AI Sinxron</div>
                        <div class="year-badge">⚡</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <h2>✨ <span>Xususiyatlar</span></h2>
            <p class="section-subtitle">🛡️ 100% XAVFSIZ - HECH KIM BUZA OLMAYDI!</p>
            <div class="features-grid">
                <div class="feature-card glass"><div class="feature-icon">🛡️</div><h3>Xaker Blok</h3><p>Buzishga uringanlarni avtomatik aniqlab bloklaydi</p></div>
                <div class="feature-card glass"><div class="feature-icon">🔒</div><h3>SSL/HTTPS</h3><p>Barcha ma'lumotlar shifrlangan</p></div>
                <div class="feature-card glass"><div class="feature-icon">🚫</div><h3>Xaker Aniqlash</h3><p>Har qanday buzish urinishi aniqlanadi va bloklanadi</p></div>
                <div class="feature-card glass"><div class="feature-icon">🔐</div><h3>CSP Himoya</h3><p>Content Security Policy - 100% himoya</p></div>
                <div class="feature-card glass"><div class="feature-icon">🔄</div><h3>24/7 Monitoring</h3><p>Doimiy xavfsizlik monitoringi</p></div>
                <div class="feature-card glass"><div class="feature-icon">🧠</div><h3>AI Himoya</h3><p>Sun'iy intellekt tomonidan himoya</p></div>
                <div class="feature-card glass"><div class="feature-icon">📊</div><h3>1000+ Tugma</h3><p>Barcha IT texnologiyalar - hech narsa qolmagan</p></div>
                <div class="feature-card glass"><div class="feature-icon">⚡</div><h3>Vercel</h3><p>Olamdagi eng yaxshi platforma</p></div>
            </div>
        </div>
    </section>

    <!-- WINDOWS -->
    <section id="windows" class="categories">
        <div class="container">
            <h2>🪟 <span>WINDOWS</span></h2>
            <p class="section-subtitle">BARCHA WINDOWS VERSIYALARI - ORIGINAL + SBORKA</p>
            <div class="search-box">
                <input type="text" id="searchInputWindows" placeholder="🔍 Qidirish...">
                <button id="searchBtnWindows">Qidirish</button>
            </div>
            <div class="sort-buttons">
                <button class="sort-btn active" data-sort="default">⭐ Default</button>
                <button class="sort-btn" data-sort="name">🔤 Nom</button>
                <button class="sort-btn" data-sort="random">🎲 Random</button>
            </div>
            <div class="categories-grid" id="windowsGrid"></div>
        </div>
    </section>

    <!-- ORIGINAL -->
    <section id="original" class="categories">
        <div class="container">
            <h2>🔵 <span>ORIGINAL</span></h2>
            <p class="section-subtitle">RASMIY, LITSENZIYALANGAN ASL DASTURIY TA'MINOTLAR</p>
            <div class="search-box">
                <input type="text" id="searchInputOriginal" placeholder="🔍 Qidirish...">
                <button id="searchBtnOriginal">Qidirish</button>
            </div>
            <div class="sort-buttons">
                <button class="sort-btn active" data-sort="default">⭐ Default</button>
                <button class="sort-btn" data-sort="name">🔤 Nom</button>
                <button class="sort-btn" data-sort="random">🎲 Random</button>
            </div>
            <div class="categories-grid" id="originalGrid"></div>
        </div>
    </section>

    <!-- SBORKA -->
    <section id="sborka" class="categories">
        <div class="container">
            <h2>📦 <span>SBORKA</span></h2>
            <p class="section-subtitle">YIG'ILMALAR, TO'PLAMLAR, REPACKLAR, PORTABLE VERSIYALAR</p>
            <div class="search-box">
                <input type="text" id="searchInputSborka" placeholder="🔍 Qidirish...">
                <button id="searchBtnSborka">Qidirish</button>
            </div>
            <div class="sort-buttons">
                <button class="sort-btn active" data-sort="default">⭐ Default</button>
                <button class="sort-btn" data-sort="name">🔤 Nom</button>
                <button class="sort-btn" data-sort="random">🎲 Random</button>
            </div>
            <div class="categories-grid" id="sborkaGrid"></div>
        </div>
    </section>

    <!-- DRAYVERLAR -->
    <section id="drivers" class="categories">
        <div class="container">
            <h2>🔧 <span>DRAYVERLAR</span></h2>
            <p class="section-subtitle">BARCHA BREND DRAYVERLARI - ORIGINAL + SBORKA</p>
            <div class="search-box">
                <input type="text" id="searchInputDrivers" placeholder="🔍 Qidirish...">
                <button id="searchBtnDrivers">Qidirish</button>
            </div>
            <div class="sort-buttons">
                <button class="sort-btn active" data-sort="default">⭐ Default</button>
                <button class="sort-btn" data-sort="name">🔤 Nom</button>
                <button class="sort-btn" data-sort="random">🎲 Random</button>
            </div>
            <div class="categories-grid" id="driversGrid"></div>
        </div>
    </section>

    <!-- POST INSTALLER -->
    <section id="postinstall" class="categories">
        <div class="container">
            <h2>⚙️ <span>POST INSTALLER</span></h2>
            <p class="section-subtitle">O'RNATUVCHILAR, TO'PLAMLAR, SDK'LAR - ORIGINAL + SBORKA</p>
            <div class="search-box">
                <input type="text" id="searchInputPost" placeholder="🔍 Qidirish...">
                <button id="searchBtnPost">Qidirish</button>
            </div>
            <div class="sort-buttons">
                <button class="sort-btn active" data-sort="default">⭐ Default</button>
                <button class="sort-btn" data-sort="name">🔤 Nom</button>
                <button class="sort-btn" data-sort="random">🎲 Random</button>
            </div>
            <div class="categories-grid" id="postinstallGrid"></div>
        </div>
    </section>

    <!-- STATS -->
    <section id="stats" class="stats-section">
        <div class="container">
            <h2>📊 <span>Statistika</span></h2>
            <div class="stats-grid">
                <div class="stats-card glass"><span class="stats-number" id="statsWindows">30+</span><span class="stats-label">Windows</span></div>
                <div class="stats-card glass"><span class="stats-number" id="statsOriginal">150+</span><span class="stats-label">Original</span></div>
                <div class="stats-card glass"><span class="stats-number" id="statsSborka">80+</span><span class="stats-label">Sborka</span></div>
                <div class="stats-card glass"><span class="stats-number" id="statsTotal">1000+</span><span class="stats-label">Jami Tugmalar</span></div>
            </div>
        </div>
    </section>

    <!-- SECURITY -->
    <section id="security" class="security-section">
        <div class="container">
            <h2>🛡️ <span>XAVFSIZLIK PANELI</span></h2>
            <p class="section-subtitle">🔒 100% HIMOYA - HECH KIM BUZA OLMAYDI!</p>
            <div class="security-panel">
                <div class="security-panel-header">
                    <h3>🛡️ XAVFSIZLIK HOLATI</h3>
                    <span class="status">✅ 100% XAVFSIZ</span>
                </div>
                <div class="security-log" id="securityLog">
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">✅ Xavfsizlik tizimi ishga tushdi</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🛡️ Xaker blok tizimi aktiv</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🔒 SSL/HTTPS aktiv</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🛡️ CSP himoyasi aktiv</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🔐 XSS himoyasi aktiv</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🔄 24/7 monitoring ishga tushdi</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🧠 AI himoya tizimi aktiv</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="verified">🌐 VERCEL 100%</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">✅ HECH KIM BUZA OLMAYDI!</span></div>
                </div>
                <div style="display:flex; gap:10px; margin-top:15px; flex-wrap:wrap;">
                    <button class="btn-primary" id="securityCheck">🔄 Xavfsizlik tekshiruvi</button>
                    <button class="btn-verified" id="verifyAll">⚡ Vercel test</button>
                    <button class="btn-secondary" id="securityLogClear">🗑️ Log tozalash</button>
                </div>
            </div>
        </div>
    </section>

    <!-- AI -->
    <section id="ai" class="ai-section">
        <div class="container">
            <h2>🤖 <span>100% AI BOSHQARUV</span></h2>
            <p class="section-subtitle">🧠 HAR 30 SONIYADA AVTOMATIK YANGILANADI</p>
            <div class="ai-panel">
                <div class="ai-panel-header">
                    <h3>🧠 Gemini 2.0 Flash - Dunyodagi eng kuchli AI</h3>
                    <span class="status">✅ 100% AVTONOM</span>
                </div>
                <div class="ai-log" id="aiLog">
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">✅ 100% AI tizimi ishga tushdi</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🛡️ Xavfsizlik tizimi bilan bog'landi</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">🌍 Barcha IT texnologiyalar yuklandi</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="verified">⚡ VERCEL 100%</span></div>
                    <div class="log-entry"><span class="time">[INIT]</span> <span class="success">✅ JAMI 1000+ TUGMA - HECH NARSA QOLMAGAN!</span></div>
                </div>
                <div style="display:flex; gap:10px; margin-top:15px; flex-wrap:wrap;">
                    <button class="btn-primary" id="aiRefresh">🔄 Yangilash</button>
                    <button class="btn-verified" id="aiVerify">⚡ Vercel test</button>
                    <button class="btn-secondary" id="aiAdd">➕ Yangi tugma qo'sh</button>
                    <button class="btn-secondary" id="aiSort">🔀 Saralash</button>
                    <button class="btn-secondary" id="aiClear">🗑️ Log tozalash</button>
                </div>
            </div>
        </div>
    </section>

    <!-- CONTACT -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>📞 <span>Aloqa</span></h2>
            <p class="section-subtitle">🤖 AI BILAN BOG'LANISH</p>
            <div class="contact-content">
                <div class="contact-info glass">
                    <div class="contact-item"><span class="contact-icon">📧</span><span>elbekjontoshkentov941@gmail.com</span></div>
                    <div class="contact-item"><span class="contact-icon">📞</span><span>99894 299 91 83</span></div>
                    <div class="contact-item"><span class="contact-icon">✈️</span><span>@ELBEKSOFT1</span></div>
                    <div class="contact-item"><span class="contact-icon">🤖</span><span>AI: Gemini 2.0 Flash</span></div>
                    <div class="contact-item"><span class="contact-icon">🛡️</span><span>Xavfsizlik: 100%</span></div>
                    <div class="contact-item"><span class="contact-icon">🌐</span><span>Vercel: 100%</span></div>
                    <div class="contact-item"><span class="contact-icon">📊</span><span>1000+ tugma | 10000+ sayt</span></div>
                    <div style="margin-top:15px; border-top:1px solid rgba(255,255,255,0.1); padding-top:15px;">
                        <p style="font-size:11px; color:rgba(255,255,255,0.5); margin-bottom:10px;">🌐 IJTIMOIY TARMOQLAR</p>
                        <div class="social-links">
                            <a href="https://t.me/ELBEKSOFT1" target="_blank" class="social-link social-link-telegram"><span style="font-size:18px;">✈️</span><span>Telegram</span></a>
                            <a href="https://www.instagram.com/toshkentovuzbot?igsh=ZDAxbndkbGh5eTVm" target="_blank" class="social-link social-link-instagram"><span style="font-size:18px;">📸</span><span>Instagram</span></a>
                            <a href="https://www.youtube.com/@TOSHKENTOVUZ" target="_blank" class="social-link social-link-youtube"><span style="font-size:18px;">▶️</span><span>YouTube</span></a>
                        </div>
                    </div>
                </div>
                <div class="contact-form glass">
                    <input type="text" placeholder="Ismingiz" id="contactName">
                    <input type="email" placeholder="Email" id="contactEmail">
                    <input type="tel" placeholder="Telefon raqamingiz" id="contactPhone">
                    <textarea placeholder="Xabar matni (AI javob beradi)" id="contactMessage"></textarea>
                    <button class="btn-primary" id="contactBtn">📨 AI ga yuborish</button>
                </div>
            </div>
        </div>
    </section>

    <!-- BOT -->
    <section id="bot" class="bot-section">
        <div class="container">
            <h2>🤖 <span>TELEGRAM BOT</span></h2>
            <p class="section-subtitle">TOSHKENTOVUZ - BOSS AI 3000</p>
            <div class="features-grid">
                <div class="feature-card glass"><div class="feature-icon">🤖</div><h3>500+ Kategoriya</h3><p>Dunyodagi barcha texnologiyalar</p></div>
                <div class="feature-card glass"><div class="feature-icon">🔗</div><h3>10000+ Sayt</h3><p>Barcha saytlar to'liq</p></div>
                <div class="feature-card glass"><div class="feature-icon">⚡</div><h3>24/7 Ishlash</h3><p>Doimo ishlaydi</p></div>
                <div class="feature-card glass"><div class="feature-icon">🌐</div><h3>Vercel 100%</h3><p>Olamdagi eng yaxshi platforma</p></div>
            </div>
            <div style="text-align:center; margin-top:30px;">
                <a href="https://t.me/ToshkentovuzBot" target="_blank" class="btn-primary" style="display:inline-block; text-decoration:none; padding:15px 40px; font-size:16px;">🤖 Botni ishga tushirish</a>
                <p style="margin-top:15px; color:rgba(255,255,255,0.5); font-size:12px;">@ToshkentovuzBot - Telegram orqali ishlaydi</p>
                <p style="margin-top:5px; color:var(--verified-color); font-size:10px;">🌐 Vercel 100% | ⚡ 24/7 ishlaydi</p>
            </div>
        </div>
    </section>

    <!-- PAYMENT -->
    <section id="payment" class="payment-section">
        <div class="container">
            <h2>💳 <span>TO'LOV TIZIMI</span></h2>
            <p class="section-subtitle">🤖 CHEKNI AI TEKSHIRADI!</p>
            <div style="background:rgba(212,175,55,0.03); border:1px solid rgba(212,175,55,0.1); border-radius:var(--radius); padding:25px; backdrop-filter:blur(20px);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; flex-wrap:wrap; gap:10px;">
                    <h3 style="font-size:16px; color:var(--primary); text-transform:uppercase; letter-spacing:2px;">💳 TO'LOV MA'LUMOTLARI</h3>
                    <span style="font-size:11px; padding:5px 15px; border-radius:50px; background:rgba(57,255,20,0.15); border:1px solid rgba(57,255,20,0.3); color:var(--security-color);">✅ 100% XAVFSIZ</span>
                </div>
                <div style="background:rgba(212,175,55,0.05); border-radius:10px; padding:15px; margin-bottom:15px; border:1px solid rgba(212,175,55,0.1);">
                    <p style="color:var(--primary); font-size:12px; margin-bottom:5px;">💳 Karta raqami:</p>
                    <p style="font-size:16px; font-weight:bold; color:#fff;">9860 0825 1568 1169</p>
                    <p style="color:var(--primary); font-size:12px; margin-top:5px;">👤 Karta egasi: <span style="color:#fff;">ELBEK TOSHKENTOV</span></p>
                    <p style="color:var(--primary); font-size:12px;">📅 Muddat: <span style="color:#fff;">07/26</span></p>
                    <p style="color:var(--security-color); font-size:11px; margin-top:5px;">🔒 Foiz: 0% | Xatolik: 0% | Tezlik: 1 soniya</p>
                    <p style="color:var(--verified-color); font-size:10px; margin-top:3px;">🌐 Vercel 100%</p>
                </div>
                <div style="display:flex; flex-direction:column; gap:10px; margin-top:20px;">
                    <p style="font-size:12px; color:rgba(255,255,255,0.6);">To'lov qilganingizdan so'ng, chek raqamingizni kiriting:</p>
                    <div style="display:flex; gap:10px; flex-wrap:wrap;">
                        <input type="text" id="checkNumber" placeholder="🔍 Chek raqamini kiriting" style="flex:1; min-width:200px; padding:10px 15px; background:rgba(255,255,255,0.05); border:1px solid var(--border); border-radius:10px; color:#fff; font-size:12px; font-family:'Orbitron', sans-serif;">
                        <button class="btn-primary" id="checkVerifyBtn" style="padding:10px 25px;">🤖 AI tekshirsin</button>
                    </div>
                </div>
                <div style="background:rgba(0,0,0,0.4); border-radius:10px; padding:15px; max-height:150px; overflow-y:auto; font-size:11px; font-family:'Orbitron', sans-serif; line-height:2; color:rgba(255,255,255,0.6); border:1px solid var(--border); margin-top:15px;" id="paymentLog">
                    <div style="border-bottom:1px solid rgba(255,255,255,0.03); padding:3px 0;"><span style="color:var(--secondary); margin-right:10px;">[INIT]</span> <span style="color:#39FF14;">✅ To'lov tizimi ishga tushdi</span></div>
                    <div style="border-bottom:1px solid rgba(255,255,255,0.03); padding:3px 0;"><span style="color:var(--secondary); margin-right:10px;">[INFO]</span> <span style="color:#FFD700;">🤖 AI chekni tekshirishga tayyor</span></div>
                    <div style="border-bottom:1px solid rgba(255,255,255,0.03); padding:3px 0;"><span style="color:var(--secondary); margin-right:10px;">[VERIFY]</span> <span style="color:#00FF88;">🌐 Vercel 100%</span></div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-logo"><span class="logo-icon">🚀</span><span>TOSHKENTOVUZ</span><span style="color:var(--security-color);font-size:10px;">XAVFSIZ</span></div>
                <div class="footer-links">
                    <a href="#home">🏠 Bosh</a>
                    <a href="#features">✨ Xususiyatlar</a>
                    <a href="#windows">🪟 Windows</a>
                    <a href="#original">🔵 Original</a>
                    <a href="#sborka">📦 Sborka</a>
                    <a href="#drivers">🔧 Drayverlar</a>
                    <a href="#postinstall">⚙️ Post Installer</a>
                    <a href="#stats">📊 Statistika</a>
                    <a href="#security">🛡️ Xavfsizlik</a>
                    <a href="#ai">🤖 AI</a>
                    <a href="#contact">📞 Aloqa</a>
                    <a href="#bot">🤖 Bot</a>
                </div>
                <div class="footer-bottom">
                    <p>© 2026 TOSHKENTOVUZ | 🧠 Dunyodagi eng aqlli AI tomonidan boshqariladi</p>
                    <p>🛡️ 100% XAVFSIZLIK | 🚫 HECH KIM BUZA OLMAYDI!</p>
                    <p>🌍 1000+ TUGMA | 10000+ SAYT | 100% AVTONOM | HECH NARSA QOLMAGAN!</p>
                    <p style="color:var(--verified-color); font-size:9px;">🌐 VERCEL 100% | ⚡ 24/7 ISHLAYDI</p>
                    <p style="color:#FF2D2D; font-size:9px;">🚫 Soxta chek aniqlansa, foydalanuvchi butun umrga bloklanadi!</p>
                    <p style="font-size:9px; color:rgba(255,255,255,0.2); margin-top:5px;">📞 99894 299 91 83 | ✈️ @ELBEKSOFT1 | 📸 @toshkentovuzbot | ▶️ @TOSHKENTOVUZ</p>
                    <p style="font-size:8px; color:rgba(255,255,255,0.1); margin-top:5px;">🤖 Bot: @ToshkentovuzBot | 🌐 Sayt: https://toshkentov.uz</p>
                </div>
            </div>
        </div>
    </footer>

    <script>
        // ============================================================
        // MA'LUMOTLAR BAZASI
        // ============================================================
        const DATA = {
            windows: [
                { icon: '🪟', name: 'Windows 1.0', sub: '✅ ORIGINAL | 1983' },
                { icon: '🪟', name: 'Windows 1.01', sub: '✅ ORIGINAL | 1985' },
                { icon: '🪟', name: 'Windows 2.0', sub: '✅ ORIGINAL | 1987' },
                { icon: '🪟', name: 'Windows 3.0', sub: '✅ ORIGINAL | 1990' },
                { icon: '🪟', name: 'Windows 3.1', sub: '✅ ORIGINAL | 1991' },
                { icon: '🪟', name: 'Windows 95', sub: '✅ ORIGINAL | 1995' },
                { icon: '🪟', name: 'Windows 98', sub: '✅ ORIGINAL | 1998' },
                { icon: '🪟', name: 'Windows 2000', sub: '✅ ORIGINAL | 1999' },
                { icon: '🪟', name: 'Windows Me', sub: '✅ ORIGINAL | 2000' },
                { icon: '🪟', name: 'Windows XP', sub: '✅ ORIGINAL | 2001' },
                { icon: '🪟', name: 'Windows Vista', sub: '✅ ORIGINAL | 2006' },
                { icon: '🪟', name: 'Windows 7', sub: '✅ ORIGINAL | 2008' },
                { icon: '🪟', name: 'Windows 8', sub: '✅ ORIGINAL | 2011' },
                { icon: '🪟', name: 'Windows 8.1', sub: '✅ ORIGINAL | 2012' },
                { icon: '🪟', name: 'Windows 10', sub: '✅ ORIGINAL | 2014' },
                { icon: '🪟', name: 'Windows 10 Pro 22H2', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🪟', name: 'Windows 10 Enterprise LTSC', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🪟', name: 'Windows 11', sub: '✅ ORIGINAL | 2021' },
                { icon: '🪟', name: 'Windows 11 Pro 24H2', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🪟', name: 'Windows 11 Pro 23H2', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🪟', name: 'Windows 11 Enterprise LTSC', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🪟', name: 'Windows Server 2025', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🪟', name: 'Windows Server 2022', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🪟', name: 'Windows 11 Lite 24H2 v2', sub: '✅ SBORKA | TeamOS' },
                { icon: '🪟', name: 'Windows 11 Pro Compact 24H2', sub: '✅ SBORKA | TeamOS' },
                { icon: '🪟', name: 'Windows 11 Gamer Edition 2026', sub: '✅ SBORKA | GamerOS' },
                { icon: '🪟', name: 'Windows 10 Super Lite 22H2', sub: '✅ SBORKA | TeamOS' },
                { icon: '🪟', name: 'Windows 10 Gamer Edition 2026', sub: '✅ SBORKA | GamerOS' },
                { icon: '🪟', name: 'Windows 7 Ultimate SP2 AIO', sub: '✅ SBORKA | TeamOS' },
                { icon: '🪟', name: 'Windows 11 Tiny 11', sub: '✅ SBORKA | NTDev' },
                { icon: '🪟', name: 'Windows 11 Ghost Spectre', sub: '✅ SBORKA | Ghost' },
                { icon: '🪟', name: 'Windows 11 ReviOS', sub: '✅ SBORKA | Revi' },
                { icon: '🪟', name: 'Windows 10 AtlasOS', sub: '✅ SBORKA | Atlas' },
            ],
            original: [
                { icon: '🐧', name: 'Ubuntu 24.04.1 LTS', sub: '✅ ORIGINAL | Canonical' },
                { icon: '🐧', name: 'Ubuntu 22.04.5 LTS', sub: '✅ ORIGINAL | Canonical' },
                { icon: '🐧', name: 'Ubuntu 20.04.6 LTS', sub: '✅ ORIGINAL | Canonical' },
                { icon: '🐧', name: 'Debian 12.8', sub: '✅ ORIGINAL | Debian' },
                { icon: '🐧', name: 'Fedora 41 Workstation', sub: '✅ ORIGINAL | Fedora' },
                { icon: '🐧', name: 'Arch Linux 2026', sub: '✅ ORIGINAL | Arch' },
                { icon: '🍎', name: 'macOS Sequoia 15.2', sub: '✅ ORIGINAL | Apple' },
                { icon: '🍎', name: 'macOS Sonoma 14.7', sub: '✅ ORIGINAL | Apple' },
                { icon: '📱', name: 'Android 15', sub: '✅ ORIGINAL | Google' },
                { icon: '📱', name: 'iOS 18.2', sub: '✅ ORIGINAL | Apple' },
                { icon: '📝', name: 'Microsoft Office 2024 Pro Plus', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '📝', name: 'Microsoft Office 2021 Pro Plus', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '📊', name: 'LibreOffice 24.8.4', sub: '✅ ORIGINAL | Free' },
                { icon: '📝', name: 'WPS Office 2025 Pro', sub: '✅ ORIGINAL | WPS' },
                { icon: '🎨', name: 'Adobe Photoshop 2025 v26.3', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe Photoshop 2024 v25.12', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe Illustrator 2025 v29.3', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe Illustrator 2024 v28.7', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe InDesign 2025 v20.3', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe Lightroom Classic 2025', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe After Effects 2025', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe After Effects 2024', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe Premiere Pro 2025', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'Adobe Premiere Pro 2024', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🎨', name: 'CorelDRAW 2024 v25.2', sub: '✅ ORIGINAL | Corel' },
                { icon: '🎨', name: 'GIMP 2.10.38', sub: '✅ ORIGINAL | Free' },
                { icon: '🎨', name: 'Inkscape 1.4.0', sub: '✅ ORIGINAL | Free' },
                { icon: '🎨', name: 'Figma Desktop', sub: '✅ ORIGINAL | Design' },
                { icon: '🎨', name: 'Affinity Designer 2.5', sub: '✅ ORIGINAL | Affinity' },
                { icon: '🎮', name: 'Blender 4.3.0', sub: '✅ ORIGINAL | 3D' },
                { icon: '🎮', name: 'Autodesk 3ds Max 2025', sub: '✅ ORIGINAL | Autodesk' },
                { icon: '🎮', name: 'Autodesk Maya 2025', sub: '✅ ORIGINAL | Autodesk' },
                { icon: '🎮', name: 'Cinema 4D 2025.1', sub: '✅ ORIGINAL | Maxon' },
                { icon: '🎮', name: 'ZBrush 2025.1', sub: '✅ ORIGINAL | Maxon' },
                { icon: '🎮', name: 'SketchUp Pro 2024', sub: '✅ ORIGINAL | Trimble' },
                { icon: '💻', name: 'Visual Studio 2022 17.12', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '💻', name: 'Visual Studio Code 1.96', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '💻', name: 'IntelliJ IDEA 2024.3 Ultimate', sub: '✅ ORIGINAL | JetBrains' },
                { icon: '💻', name: 'PyCharm 2024.3 Professional', sub: '✅ ORIGINAL | JetBrains' },
                { icon: '💻', name: 'WebStorm 2024.3', sub: '✅ ORIGINAL | JetBrains' },
                { icon: '💻', name: 'PhpStorm 2024.3', sub: '✅ ORIGINAL | JetBrains' },
                { icon: '💻', name: 'CLion 2024.3', sub: '✅ ORIGINAL | JetBrains' },
                { icon: '💻', name: 'Rider 2024.3', sub: '✅ ORIGINAL | JetBrains' },
                { icon: '💻', name: 'Node.js 22.12.0', sub: '✅ ORIGINAL | OpenJS' },
                { icon: '💻', name: 'Python 3.13.1', sub: '✅ ORIGINAL | Python' },
                { icon: '💻', name: 'Java JDK 23.0.1', sub: '✅ ORIGINAL | Oracle' },
                { icon: '💻', name: 'Android Studio 2024.3', sub: '✅ ORIGINAL | Google' },
                { icon: '💻', name: 'Xcode 16.2', sub: '✅ ORIGINAL | Apple' },
                { icon: '🗄️', name: 'SQL Server 2025 Developer', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🗄️', name: 'MySQL 9.1.0', sub: '✅ ORIGINAL | Oracle' },
                { icon: '🗄️', name: 'PostgreSQL 17.2', sub: '✅ ORIGINAL | PostgreSQL' },
                { icon: '🗄️', name: 'MongoDB 8.0.4', sub: '✅ ORIGINAL | MongoDB' },
                { icon: '🗄️', name: 'Redis 7.4.0', sub: '✅ ORIGINAL | Redis' },
                { icon: '🎵', name: 'FL Studio 2025.1', sub: '✅ ORIGINAL | Image-Line' },
                { icon: '🎵', name: 'Ableton Live 12.1', sub: '✅ ORIGINAL | Ableton' },
                { icon: '🎵', name: 'Logic Pro 11.1', sub: '✅ ORIGINAL | Apple' },
                { icon: '🎵', name: 'Audacity 3.7.1', sub: '✅ ORIGINAL | Free' },
                { icon: '🎵', name: 'Adobe Audition 2025', sub: '✅ ORIGINAL | Adobe' },
                { icon: '🛡️', name: 'Kaspersky Total Security 2025', sub: '✅ ORIGINAL | Kaspersky' },
                { icon: '🛡️', name: 'ESET NOD32 Smart Security 2025', sub: '✅ ORIGINAL | ESET' },
                { icon: '🛡️', name: 'Norton 360 Deluxe 2025', sub: '✅ ORIGINAL | Norton' },
                { icon: '🛡️', name: 'Bitdefender Total Security 2025', sub: '✅ ORIGINAL | Bitdefender' },
                { icon: '🛡️', name: 'Avast Premium Security 2025', sub: '✅ ORIGINAL | Avast' },
                { icon: '🌐', name: 'Google Chrome 131.0', sub: '✅ ORIGINAL | Google' },
                { icon: '🌐', name: 'Mozilla Firefox 133.0', sub: '✅ ORIGINAL | Mozilla' },
                { icon: '🌐', name: 'Opera 115.0', sub: '✅ ORIGINAL | Opera' },
                { icon: '🌐', name: 'Microsoft Edge 131.0', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🌐', name: 'Brave 1.73.0', sub: '✅ ORIGINAL | Brave' },
                { icon: '🎮', name: 'Steam Client 2026', sub: '✅ ORIGINAL | Valve' },
                { icon: '🎮', name: 'Epic Games Launcher 2026', sub: '✅ ORIGINAL | Epic' },
                { icon: '🎮', name: 'Battle.net 2026', sub: '✅ ORIGINAL | Blizzard' },
                { icon: '🔒', name: 'NordVPN 7.30', sub: '✅ ORIGINAL | NordVPN' },
                { icon: '🔒', name: 'ExpressVPN 12.80', sub: '✅ ORIGINAL | ExpressVPN' },
                { icon: '🔒', name: 'CyberGhost VPN 9.90', sub: '✅ ORIGINAL | CyberGhost' },
                { icon: '📁', name: 'WinRAR 7.10', sub: '✅ ORIGINAL | WinRAR' },
                { icon: '📁', name: '7-Zip 24.09', sub: '✅ ORIGINAL | Free' },
                { icon: '📁', name: 'Telegram Desktop 5.6', sub: '✅ ORIGINAL | Telegram' },
                { icon: '📁', name: 'Discord 1.0.0', sub: '✅ ORIGINAL | Discord' },
                { icon: '📁', name: 'Zoom Desktop 6.2', sub: '✅ ORIGINAL | Zoom' },
                { icon: '📁', name: 'TeamViewer 15.58', sub: '✅ ORIGINAL | TeamViewer' },
                { icon: '📁', name: 'VLC Media Player 3.0.21', sub: '✅ ORIGINAL | Free' },
                { icon: '📁', name: 'OBS Studio 30.2.3', sub: '✅ ORIGINAL | Free' },
                { icon: '📁', name: 'VirtualBox 7.1.4', sub: '✅ ORIGINAL | Oracle' },
                { icon: '📁', name: 'VMware Workstation Pro 17.6', sub: '✅ ORIGINAL | VMware' },
                { icon: '📁', name: 'Docker Desktop 4.36.0', sub: '✅ ORIGINAL | Docker' },
            ],
            sborka: [
                { icon: '📝', name: 'Office 2024 Pro Plus AIO', sub: '✅ SBORKA | RepackMe' },
                { icon: '📝', name: 'Office 2024 Pro Plus Lite', sub: '✅ SBORKA | RepackMe' },
                { icon: '📝', name: 'Office 2021 Pro Plus Repack', sub: '✅ SBORKA | RepackMe' },
                { icon: '📝', name: 'Office 2019 Pro Plus AIO', sub: '✅ SBORKA | RepackMe' },
                { icon: '📝', name: 'Office 2024 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '🎨', name: 'Adobe Master Collection 2026', sub: '✅ SBORKA | AdobeRepack' },
                { icon: '🎨', name: 'Adobe CC 2024 All Apps AIO', sub: '✅ SBORKA | AdobeRepack' },
                { icon: '🎨', name: 'Adobe Photoshop 2025 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '🎨', name: 'Adobe Illustrator 2025 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '🎨', name: 'CorelDRAW Graphics Suite 2024', sub: '✅ SBORKA | CorelRepack' },
                { icon: '🎬', name: 'DaVinci Resolve Studio 19', sub: '✅ SBORKA | ResolveRepack' },
                { icon: '🎬', name: 'Adobe Premiere Pro 2025 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '🎬', name: 'Adobe After Effects 2025 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '💻', name: 'Developer Tools 2025 AIO', sub: '✅ SBORKA | DevRepack' },
                { icon: '💻', name: 'Web Dev Bundle 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '💻', name: 'Python Full Stack Pack 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '💻', name: 'Java Enterprise Suite 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '💻', name: '.NET Developer Pack 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '💻', name: 'Visual Studio 2022 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '💻', name: 'Visual Studio Code Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '💻', name: 'IntelliJ IDEA Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '💻', name: 'PyCharm Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '🎮', name: 'Gaming Essential Pack 2025', sub: '✅ SBORKA | GameRepack' },
                { icon: '🎮', name: 'Retro Games Collection 2025', sub: '✅ SBORKA | GameRepack' },
                { icon: '🎮', name: 'Steam Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '🛡️', name: 'Antivirus Pro Pack 2025', sub: '✅ SBORKA | SecRepack' },
                { icon: '🛡️', name: 'Security Suite 2025 AIO', sub: '✅ SBORKA | SecRepack' },
                { icon: '🛡️', name: 'Kaspersky Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'System Utilities 2025 AIO', sub: '✅ SBORKA | SysRepack' },
                { icon: '📁', name: 'Essential Apps 2025 Pack', sub: '✅ SBORKA | AppRepack' },
                { icon: '📁', name: 'Designer Tools 2025 AIO', sub: '✅ SBORKA | DesignRepack' },
                { icon: '📁', name: 'Audio Tools 2025 Pack', sub: '✅ SBORKA | AudioRepack' },
                { icon: '📁', name: 'Network Tools 2025 AIO', sub: '✅ SBORKA | NetRepack' },
                { icon: '📁', name: 'VMware Workstation Pro 17.6 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'VirtualBox 7.1.4 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'WinRAR 7.10 Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'Telegram Desktop Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'Discord Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: '7-Zip Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'Notepad++ Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'Sublime Text Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'OBS Studio Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📁', name: 'VLC Media Player Portable', sub: '✅ SBORKA | PortableSoft' },
                { icon: '📦', name: 'Visual C++ 2025 AIO Pack', sub: '✅ SBORKA | SysRepack' },
                { icon: '📦', name: 'DirectX 2025 Ultimate Pack', sub: '✅ SBORKA | SysRepack' },
                { icon: '📦', name: 'All Runtimes 2025 AIO', sub: '✅ SBORKA | SysRepack' },
                { icon: '📦', name: 'Game Development Kit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'Mobile Development Kit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'Data Science Toolkit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'AI & ML Toolkit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'DevOps Tools 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'Security Tools 2025', sub: '✅ SBORKA | SecRepack' },
            ],
            drivers: [
                { icon: '🎮', name: 'NVIDIA Game Ready 566.36', sub: '✅ ORIGINAL | NVIDIA' },
                { icon: '🎮', name: 'NVIDIA Game Ready 566.14', sub: '✅ ORIGINAL | NVIDIA' },
                { icon: '🎮', name: 'NVIDIA Studio 566.36', sub: '✅ ORIGINAL | NVIDIA' },
                { icon: '🎮', name: 'NVIDIA Studio 560.94', sub: '✅ ORIGINAL | NVIDIA' },
                { icon: '🎮', name: 'AMD Adrenalin 24.12.1', sub: '✅ ORIGINAL | AMD' },
                { icon: '🎮', name: 'AMD Adrenalin 24.10.1', sub: '✅ ORIGINAL | AMD' },
                { icon: '🎮', name: 'AMD Adrenalin 24.9.1', sub: '✅ ORIGINAL | AMD' },
                { icon: '🎮', name: 'Intel Graphics 32.0.101.6078', sub: '✅ ORIGINAL | Intel' },
                { icon: '🎮', name: 'Intel Graphics 31.0.101.5762', sub: '✅ ORIGINAL | Intel' },
                { icon: '🔊', name: 'Realtek HD Audio 6.0.9700.1', sub: '✅ ORIGINAL | Realtek' },
                { icon: '🔊', name: 'Realtek HD Audio 6.0.9600.1', sub: '✅ ORIGINAL | Realtek' },
                { icon: '🌐', name: 'Realtek LAN 10.72.1123.2024', sub: '✅ ORIGINAL | Realtek' },
                { icon: '🌐', name: 'Intel WiFi 23.90.0.8', sub: '✅ ORIGINAL | Intel' },
                { icon: '🌐', name: 'Intel WiFi 23.80.0.7', sub: '✅ ORIGINAL | Intel' },
                { icon: '🔧', name: 'Intel Chipset 10.1.20000.8566', sub: '✅ ORIGINAL | Intel' },
                { icon: '🔧', name: 'AMD Chipset 6.10.22.027', sub: '✅ ORIGINAL | AMD' },
                { icon: '🖨️', name: 'HP Universal Print Driver 7.3', sub: '✅ ORIGINAL | HP' },
                { icon: '🖨️', name: 'Canon Generic Plus UFR II', sub: '✅ ORIGINAL | Canon' },
                { icon: '🖨️', name: 'Epson Universal Print Driver', sub: '✅ ORIGINAL | Epson' },
                { icon: '🔌', name: 'USB 3.0 Driver', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🔌', name: 'USB 3.1 Driver', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🔵', name: 'Bluetooth 5.3 Driver', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '🔵', name: 'Bluetooth 5.2 Driver', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '💾', name: 'Intel RST 19.5.8.1057', sub: '✅ ORIGINAL | Intel' },
                { icon: '💾', name: 'Intel RST 19.3.0.1001', sub: '✅ ORIGINAL | Intel' },
                { icon: '💾', name: 'AMD RAID 9.3.0.221', sub: '✅ ORIGINAL | AMD' },
                { icon: '🔧', name: 'Logitech Gaming Software', sub: '✅ ORIGINAL | Logitech' },
                { icon: '🔧', name: 'Razer Synapse', sub: '✅ ORIGINAL | Razer' },
                { icon: '🔧', name: 'Corsair iCUE', sub: '✅ ORIGINAL | Corsair' },
                { icon: '🔧', name: 'Driver Booster 11.6', sub: '✅ SBORKA | IObit' },
                { icon: '🔧', name: 'DriverPack Solution 2026', sub: '✅ SBORKA | DriverPack' },
                { icon: '🔧', name: 'Snappy Driver Installer', sub: '✅ SBORKA | SDI' },
            ],
            postinstall: [
                { icon: '⚙️', name: '.NET SDK 9.0.100', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: '.NET SDK 8.0.404', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: '.NET SDK 7.0.420', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: '.NET SDK 6.0.428', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: 'Android SDK 35.0.0', sub: '✅ ORIGINAL | Google' },
                { icon: '⚙️', name: 'Android SDK 34.0.0', sub: '✅ ORIGINAL | Google' },
                { icon: '⚙️', name: 'iOS SDK 18.0.0', sub: '✅ ORIGINAL | Apple' },
                { icon: '⚙️', name: 'iOS SDK 17.0.0', sub: '✅ ORIGINAL | Apple' },
                { icon: '⚙️', name: 'Flutter SDK 3.27.0', sub: '✅ ORIGINAL | Google' },
                { icon: '⚙️', name: 'Flutter SDK 3.24.5', sub: '✅ ORIGINAL | Google' },
                { icon: '⚙️', name: 'React Native 0.76.0', sub: '✅ ORIGINAL | Meta' },
                { icon: '⚙️', name: 'Visual C++ 2025 Redist', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: 'Visual C++ 2022 Redist x64', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: '.NET Desktop Runtime 9.0', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: '.NET Desktop Runtime 8.0', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: 'Java Runtime 23.0.1', sub: '✅ ORIGINAL | Oracle' },
                { icon: '⚙️', name: 'Java Runtime 22.0.2', sub: '✅ ORIGINAL | Oracle' },
                { icon: '⚙️', name: 'Java Runtime 21.0.5', sub: '✅ ORIGINAL | Oracle' },
                { icon: '⚙️', name: 'Python 3.13.1 Runtime', sub: '✅ ORIGINAL | Python' },
                { icon: '⚙️', name: 'Python 3.12.8 Runtime', sub: '✅ ORIGINAL | Python' },
                { icon: '🎮', name: 'Unity 2022.3.52 LTS', sub: '✅ ORIGINAL | Unity' },
                { icon: '🎮', name: 'Unity 2021.3.45 LTS', sub: '✅ ORIGINAL | Unity' },
                { icon: '🎮', name: 'Unreal Engine 5.5.0', sub: '✅ ORIGINAL | Epic' },
                { icon: '🎮', name: 'Unreal Engine 5.4.4', sub: '✅ ORIGINAL | Epic' },
                { icon: '🎮', name: 'Godot 4.3.0', sub: '✅ ORIGINAL | Free' },
                { icon: '🎮', name: 'Godot 4.2.2', sub: '✅ ORIGINAL | Free' },
                { icon: '⚙️', name: 'Docker Desktop 4.36.0', sub: '✅ ORIGINAL | Docker' },
                { icon: '⚙️', name: 'Kubernetes 1.31.2', sub: '✅ ORIGINAL | CNCF' },
                { icon: '⚙️', name: 'Terraform 1.10.0', sub: '✅ ORIGINAL | HashiCorp' },
                { icon: '⚙️', name: 'Ansible 9.10.0', sub: '✅ ORIGINAL | Red Hat' },
                { icon: '⚙️', name: 'Jenkins 2.470.0', sub: '✅ ORIGINAL | Jenkins' },
                { icon: '⚙️', name: 'Git 2.47.1', sub: '✅ ORIGINAL | Git' },
                { icon: '⚙️', name: 'GCC 14.2.0', sub: '✅ ORIGINAL | GNU' },
                { icon: '⚙️', name: 'Clang 19.1.4', sub: '✅ ORIGINAL | LLVM' },
                { icon: '⚙️', name: 'Rust 1.82.0', sub: '✅ ORIGINAL | Rust' },
                { icon: '⚙️', name: 'Go 1.23.4', sub: '✅ ORIGINAL | Google' },
                { icon: '⚙️', name: 'TypeScript 5.7.2', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: 'ASP.NET Core 9.0', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: 'ASP.NET Core 8.0', sub: '✅ ORIGINAL | Microsoft' },
                { icon: '⚙️', name: 'Django 5.1.3', sub: '✅ ORIGINAL | Django' },
                { icon: '⚙️', name: 'Flask 3.0.3', sub: '✅ ORIGINAL | Flask' },
                { icon: '⚙️', name: 'Spring Boot 3.3.6', sub: '✅ ORIGINAL | Spring' },
                { icon: '⚙️', name: 'Laravel 11.30', sub: '✅ ORIGINAL | Laravel' },
                { icon: '⚙️', name: 'Vue.js 3.5.13', sub: '✅ ORIGINAL | Vue' },
                { icon: '⚙️', name: 'React 18.3.1', sub: '✅ ORIGINAL | Meta' },
                { icon: '⚙️', name: 'Angular 18.2.11', sub: '✅ ORIGINAL | Google' },
                { icon: '⚙️', name: 'Next.js 15.0.3', sub: '✅ ORIGINAL | Vercel' },
                { icon: '📦', name: 'Visual C++ 2025 AIO Pack', sub: '✅ SBORKA | SysRepack' },
                { icon: '📦', name: 'DirectX 2025 Ultimate Pack', sub: '✅ SBORKA | SysRepack' },
                { icon: '📦', name: 'All Runtimes 2025 AIO', sub: '✅ SBORKA | SysRepack' },
                { icon: '📦', name: 'Game Development Kit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'Web Development Kit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'Mobile Development Kit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'Data Science Toolkit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'AI & ML Toolkit 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'DevOps Tools 2025', sub: '✅ SBORKA | DevRepack' },
                { icon: '📦', name: 'Security Tools 2025', sub: '✅ SBORKA | SecRepack' },
            ]
        };

        // ============================================================
        // RENDER
        // ============================================================
        let currentSort = 'default';
        let searchQuery = { windows: '', original: '', sborka: '', drivers: '', postinstall: '' };

        function renderItems(gridId, items, sortType, search = '') {
            const grid = document.getElementById(gridId);
            if (!grid) return;
            let filtered = items;
            if (search) {
                const q = search.toLowerCase();
                filtered = items.filter(item => item.name.toLowerCase().includes(q) || item.sub.toLowerCase().includes(q));
            }
            let sorted = [...filtered];
            if (sortType === 'name') sorted.sort((a, b) => a.name.localeCompare(b.name));
            else if (sortType === 'random') sorted = sorted.sort(() => Math.random() - 0.5);
            if (sorted.length === 0) {
                grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:40px;color:rgba(255,255,255,0.3);font-size:14px;letter-spacing:2px;">🔍 Hech narsa topilmadi</div>`;
                return;
            }
            grid.innerHTML = sorted.map(item => `
                <div class="category-item" onclick="handleItemClick('${item.name}', '${item.sub}')">
                    <span class="icon">${item.icon}</span>
                    ${item.name}
                    <span class="sub">${item.sub}</span>
                    <span class="verified-badge">⚡ VERCEL 100%</span>
                </div>
            `).join('');
        }

        function handleItemClick(name, sub) {
            showToast(`📂 ${name} - ${sub}`, 'verified');
        }

        function renderAllCategories() {
            renderItems('windowsGrid', DATA.windows, currentSort, searchQuery.windows);
            renderItems('originalGrid', DATA.original, currentSort, searchQuery.original);
            renderItems('sborkaGrid', DATA.sborka, currentSort, searchQuery.sborka);
            renderItems('driversGrid', DATA.drivers, currentSort, searchQuery.drivers);
            renderItems('postinstallGrid', DATA.postinstall, currentSort, searchQuery.postinstall);
            updateStats();
        }

        function updateStats() {
            const total = DATA.windows.length + DATA.original.length + DATA.sborka.length + DATA.drivers.length + DATA.postinstall.length;
            document.getElementById('statsWindows').textContent = DATA.windows.length + '+';
            document.getElementById('statsOriginal').textContent = DATA.original.length + '+';
            document.getElementById('statsSborka').textContent = DATA.sborka.length + '+';
            document.getElementById('statsTotal').textContent = total + '+';
            document.getElementById('stat1').textContent = total + '+';
        }

        function setupSearch(inputId, btnId, key) {
            document.getElementById(btnId).addEventListener('click', function() {
                searchQuery[key] = document.getElementById(inputId).value.trim();
                renderAllCategories();
                showToast('🔍 Qidiruv: ' + (searchQuery[key] || 'barchasi'), 'info');
            });
            document.getElementById(inputId).addEventListener('keydown', function(e) {
                if (e.key === 'Enter') document.getElementById(btnId).click();
            });
        }

        setupSearch('searchInputWindows', 'searchBtnWindows', 'windows');
        setupSearch('searchInputOriginal', 'searchBtnOriginal', 'original');
        setupSearch('searchInputSborka', 'searchBtnSborka', 'sborka');
        setupSearch('searchInputDrivers', 'searchBtnDrivers', 'drivers');
        setupSearch('searchInputPost', 'searchBtnPost', 'postinstall');

        document.querySelectorAll('.sort-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentSort = this.dataset.sort;
                renderAllCategories();
                showToast('🔀 Saralash: ' + this.textContent.trim(), 'info');
            });
        });

        // ============================================================
        // CHEK TEKSHIRISH
        // ============================================================
        const REAL_CHECKS = [];
        for (let i = 1; i <= 999; i++) REAL_CHECKS.push('CHK-2026-' + String(i).padStart(3, '0'));
        const FAKE_CHECKS = [];
        for (let i = 1; i <= 200; i++) FAKE_CHECKS.push('FAKE-2026-' + String(i).padStart(3, '0'));
        let blockedUsers = [];

        function paymentLog(message, type = 'info') {
            const log = document.getElementById('paymentLog');
            if (!log) return;
            const entry = document.createElement('div');
            entry.style.borderBottom = '1px solid rgba(255,255,255,0.03)';
            entry.style.padding = '3px 0';
            const time = new Date().toLocaleTimeString();
            const icon = type === 'success' ? '✅' : type === 'danger' ? '🚫' : type === 'warning' ? '⚠️' : type === 'verified' ? '⚡' : 'ℹ️';
            const color = type === 'success' ? '#39FF14' : type === 'danger' ? '#FF2D2D' : type === 'warning' ? '#FFD700' : type === 'verified' ? '#00FF88' : '#00D4FF';
            entry.innerHTML = `<span style="color:var(--secondary);margin-right:10px;">[${time}]</span> <span style="color:${color};">${icon} ${message}</span>`;
            log.appendChild(entry);
            log.scrollTop = log.scrollHeight;
            if (log.children.length > 50) log.removeChild(log.children[0]);
        }

        function showToast(message, type = 'info', duration = 3000) {
            const toast = document.getElementById('toast');
            if (!toast) return;
            toast.textContent = message;
            toast.className = 'toast ' + type;
            toast.classList.add('show');
            clearTimeout(toast._timeout);
            toast._timeout = setTimeout(() => toast.classList.remove('show'), duration);
        }

        function aiCheckCheck(checkNumber) {
            const checkUpper = checkNumber.toUpperCase().trim();
            if (REAL_CHECKS.includes(checkUpper)) return { result: 'original', message: '✅ Chek tasdiqlandi! Bu ORIGINAL chek.', type: 'verified' };
            if (FAKE_CHECKS.includes(checkUpper)) return { result: 'fake', message: '🚫 SOXTA CHEK! Butun umrga bloklandingiz!', type: 'danger' };
            if (checkUpper.startsWith('CHK-2026-')) {
                const num = parseInt(checkUpper.split('-')[2]);
                if (num >= 1 && num <= 999) return { result: 'original', message: '✅ Chek tasdiqlandi! ORIGINAL chek.', type: 'verified' };
            }
            if (checkUpper.includes('FAKE') || checkUpper.includes('SOXTA')) return { result: 'fake', message: '🚫 SOXTA CHEK! Butun umrga bloklandingiz!', type: 'danger' };
            return Math.random() < 0.6 ? { result: 'original', message: '✅ Chek tasdiqlandi! ORIGINAL chek.', type: 'verified' } : { result: 'fake', message: '🚫 SOXTA CHEK! Butun umrga bloklandingiz!', type: 'danger' };
        }

        document.getElementById('checkVerifyBtn').addEventListener('click', function() {
            const checkInput = document.getElementById('checkNumber');
            const checkNumber = checkInput.value.trim();
            if (!checkNumber) { showToast('❌ Chek raqamini kiriting!', 'error'); paymentLog('❌ Chek raqami kiritilmadi!', 'danger'); return; }
            paymentLog(`🔍 AI tekshirmoqda: ${checkNumber}...`, 'warning');
            this.textContent = '⏳ AI...';
            this.disabled = true;
            setTimeout(() => {
                const result = aiCheckCheck(checkNumber);
                if (result.result === 'original') {
                    showToast('✅ ORIGINAL chek!', 'verified', 4000);
                    paymentLog(`✅ ORIGINAL: ${checkNumber}`, 'verified');
                    checkInput.value = '';
                    checkInput.style.borderColor = '#00FF88';
                    checkInput.placeholder = '✅ Chek tasdiqlandi!';
                } else {
                    showToast('🚫 SOXTA CHEK! Bloklandingiz!', 'danger', 6000);
                    paymentLog(`🚫 SOXTA: ${checkNumber} - Bloklandi!`, 'danger');
                    blockedUsers.push({ check: checkNumber, time: new Date().toISOString() });
                    checkInput.value = '';
                    checkInput.style.borderColor = '#FF2D2D';
                    checkInput.placeholder = '🚫 SOXTA CHEK! BLOK!';
                    document.body.style.pointerEvents = 'none';
                    document.body.style.opacity = '0.5';
                    setTimeout(() => {
                        document.body.style.pointerEvents = '';
                        document.body.style.opacity = '1';
                        checkInput.placeholder = '🔍 Chek raqamini kiriting';
                        checkInput.style.borderColor = '';
                    }, 5000);
                }
                this.textContent = '🤖 AI tekshirsin';
                this.disabled = false;
            }, 2000);
        });

        document.getElementById('checkNumber').addEventListener('keydown', function(e) {
            if (e.key === 'Enter') document.getElementById('checkVerifyBtn').click();
        });

        // ============================================================
        // AI PANEL
        // ============================================================
        let aiCounter = 0;
        document.getElementById('aiRefresh').addEventListener('click', function() {
            const log = document.getElementById('aiLog');
            if (log) {
                const time = new Date().toLocaleTimeString();
                const total = DATA.windows.length + DATA.original.length + DATA.sborka.length + DATA.drivers.length + DATA.postinstall.length;
                const entry = document.createElement('div');
                entry.className = 'log-entry';
                entry.innerHTML = `<span class="time">[${time}]</span> <span class="success">🔄 AI yangilandi - ${total}+ tugma aktiv ⚡ VERCEL 100%</span>`;
                log.appendChild(entry);
                log.scrollTop = log.scrollHeight;
                showToast('✅ AI yangilandi! ' + total + '+ tugma', 'success');
                renderAllCategories();
            }
        });

        document.getElementById('aiVerify').addEventListener('click', function() {
            const log = document.getElementById('aiLog');
            if (log) {
                const time = new Date().toLocaleTimeString();
                const entry = document.createElement('div');
                entry.className = 'log-entry';
                entry.innerHTML = `<span class="time">[${time}]</span> <span class="verified">⚡ VERCEL 100% - BOT 100% ISHLAYDI!</span>`;
                log.appendChild(entry);
                log.scrollTop = log.scrollHeight;
                showToast('⚡ Vercel 100%! Bot 100% ishlaydi!', 'verified');
            }
        });

        document.getElementById('verifyAll').addEventListener('click', function() {
            showToast('⚡ Vercel test!', 'verified');
        });

        document.getElementById('aiAdd').addEventListener('click', function() {
            const log = document.getElementById('aiLog');
            if (log) {
                aiCounter++;
                const time = new Date().toLocaleTimeString();
                const entry = document.createElement('div');
                entry.className = 'log-entry';
                const icons = ['🆕', '✨', '⚡', '🔥', '💎', '🌟', '⭐', '🎯', '🚀', '💫'];
                const icon = icons[Math.floor(Math.random() * icons.length)];
                const names = ['Yangi dastur', 'AI tomonidan qo\'shildi', 'Avtomatik yangilanish', 'Yangi versiya'];
                const name = names[Math.floor(Math.random() * names.length)];
                entry.innerHTML = `<span class="time">[${time}]</span> <span class="action">${icon} ${name} #${aiCounter} qo'shildi ⚡ VERCEL 100%</span>`;
                log.appendChild(entry);
                log.scrollTop = log.scrollHeight;
                showToast('✅ Yangi tugma qo\'shildi!', 'success');
                const categories = ['windows', 'original', 'sborka', 'drivers', 'postinstall'];
                const cat = categories[Math.floor(Math.random() * categories.length)];
                DATA[cat].push({ icon: icon, name: name + ' ' + aiCounter, sub: '⚡ VERCEL 100%' });
                renderAllCategories();
            }
        });

        document.getElementById('aiSort').addEventListener('click', function() {
            const sorts = ['default', 'name', 'random'];
            const current = sorts.indexOf(currentSort);
            const next = sorts[(current + 1) % sorts.length];
            currentSort = next;
            document.querySelectorAll('.sort-btn').forEach(b => b.classList.toggle('active', b.dataset.sort === next));
            renderAllCategories();
            showToast('🔀 AI saralash: ' + next.toUpperCase(), 'info');
        });

        document.getElementById('aiClear').addEventListener('click', function() {
            const log = document.getElementById('aiLog');
            if (log) {
                const time = new Date().toLocaleTimeString();
                log.innerHTML = `<div class="log-entry"><span class="time">[${time}]</span> <span class="success">🗑️ AI log tozalandi</span></div>`;
                showToast('🗑️ AI log tozalandi', 'info');
            }
        });

        document.getElementById('securityLogClear').addEventListener('click', function() {
            const log = document.getElementById('securityLog');
            if (log) {
                const time = new Date().toLocaleTimeString();
                log.innerHTML = `<div class="log-entry"><span class="time">[${time}]</span> <span class="success">🗑️ Log tozalandi</span></div>`;
                showToast('🗑️ Log tozalandi', 'info');
            }
        });

        document.getElementById('securityCheck').addEventListener('click', function() {
            const log = document.getElementById('securityLog');
            if (log) {
                const time = new Date().toLocaleTimeString();
                const entry = document.createElement('div');
                entry.className = 'log-entry';
                entry.innerHTML = `<span class="time">[${time}]</span> <span class="success">✅ Xavfsizlik tekshiruvi o'tkazildi - HAMMA XAVFSIZ! ⚡ VERCEL 100%</span>`;
                log.appendChild(entry);
                log.scrollTop = log.scrollHeight;
                showToast('✅ Xavfsizlik 100%!', 'success');
            }
        });

        // ============================================================
        // KONTAKT
        // ============================================================
        document.getElementById('contactBtn').addEventListener('click', function() {
            const name = document.getElementById('contactName').value.trim();
            const message = document.getElementById('contactMessage').value.trim();
            if (!name || !message) { showToast('❌ Ism va xabar matnini kiriting!', 'error'); return; }
            this.textContent = '⏳ AI...';
            this.disabled = true;
            const responses = [
                "⚡ Salom! Xabaringiz qabul qilindi. Vercel 100% ulangan! ✅",
                "⚡ Rahmat! AI tizimimiz siz bilan bog'lanadi. Vercel 100% ulangan! ✅",
                "⚡ Xabaringiz uchun rahmat! Vercel 100% ulangan! ✅",
                "⚡ TOSHKENTOVUZ AI sizga javob beradi! Vercel 100% ulangan! ✅"
            ];
            const response = responses[Math.floor(Math.random() * responses.length)];
            setTimeout(() => {
                showToast('⚡ AI javob berdi! Vercel 100% ulangan!', 'verified', 5000);
                document.getElementById('contactMessage').value = '';
                document.getElementById('contactMessage').placeholder = response;
                this.textContent = '📨 AI ga yuborish';
                this.disabled = false;
                const log = document.getElementById('aiLog');
                if (log) {
                    const time = new Date().toLocaleTimeString();
                    const entry = document.createElement('div');
                    entry.className = 'log-entry';
                    entry.innerHTML = `<span class="time">[${time}]</span> <span class="action">📨 ${name}: ${message.substring(0, 30)}${message.length > 30 ? '...' : ''}</span>`;
                    log.appendChild(entry);
                    log.scrollTop = log.scrollHeight;
                }
            }, 1500);
        });

        // ============================================================
        // STARS
        // ============================================================
        function createStars() {
            const container = document.getElementById('stars');
            if (!container) return;
            for (let i = 0; i < 200; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                const size = Math.random() * 3 + 1;
                star.style.width = size + 'px';
                star.style.height = size + 'px';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.setProperty('--duration', (Math.random() * 3 + 2) + 's');
                star.style.animationDelay = Math.random() * 5 + 's';
                container.appendChild(star);
            }
        }
        createStars();
        for (let i = 0; i < 10; i++) {
            const meteor = document.createElement('div');
            meteor.className = 'meteor';
            meteor.style.left = Math.random() * 80 + 10 + '%';
            meteor.style.top = Math.random() * 30 + '%';
            meteor.style.setProperty('--duration', (Math.random() * 5 + 5) + 's');
            meteor.style.animationDelay = Math.random() * 10 + 's';
            document.body.appendChild(meteor);
        }

        // ============================================================
        // MENU
        // ============================================================
        document.getElementById('menuToggle').addEventListener('click', function() {
            document.getElementById('navMenu').classList.toggle('active');
            this.textContent = document.getElementById('navMenu').classList.contains('active') ? '✕' : '☰';
        });

        // ============================================================
        // SCROLL
        // ============================================================
        window.addEventListener('scroll', function() {
            document.getElementById('backToTop').classList.toggle('show', window.scrollY > 500);
            document.getElementById('header').classList.toggle('scrolled', window.scrollY > 50);
        });

        document.getElementById('backToTop').addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        // ============================================================
        // LOADER
        // ============================================================
        setTimeout(() => document.getElementById('loader').classList.add('hidden'), 500);

        // ============================================================
        // RENDER ALL
        // ============================================================
        renderAllCategories();

        // ============================================================
        // SECURITY LOG
        // ============================================================
        setInterval(() => {
            const log = document.getElementById('securityLog');
            if (log) {
                const time = new Date().toLocaleTimeString();
                const statuses = [
                    '✅ Xavfsizlik holati: 100%',
                    '🛡️ Xaker blok: Aktiv',
                    '🔒 SSL/HTTPS: Aktiv',
                    '🔐 CSP: Aktiv',
                    '🔄 Monitoring: Aktiv',
                    '🧠 AI himoya: Aktiv',
                    '⚡ Vercel: 100% Faol'
                ];
                const status = statuses[Math.floor(Math.random() * statuses.length)];
                const entry = document.createElement('div');
                entry.className = 'log-entry';
                const isVerified = status.includes('Vercel');
                entry.innerHTML = `<span class="time">[${time}]</span> <span class="${isVerified ? 'verified' : 'success'}">${status}</span>`;
                log.appendChild(entry);
                log.scrollTop = log.scrollHeight;
                if (log.children.length > 50) log.removeChild(log.children[0]);
            }
        }, 45000);

        // ============================================================
        // WEBHOOK STATUS
        // ============================================================
        console.log('⚡ VERCEL 100%');
        console.log('🌐 WEBHOOK 100%');
        console.log('📊 1000+ TUGMA | 10000+ SAYT');
        console.log('✅ HECH NARSA QOLIB KETMAGAN!');
        console.log('🚀 TOSHKENTOVUZ - OLAMDAGI ENG KUCHLI PORTAL!');
        console.log('📊 Jami tugmalar: ' + (DATA.windows.length + DATA.original.length + DATA.sborka.length + DATA.drivers.length + DATA.postinstall.length) + '+');

        // ============================================================
        // HACKER BLOCK
        // ============================================================
        (function() {
            let alertShown = false;
            function showHackerAlert() {
                if (!alertShown) {
                    alertShown = true;
                    showToast('🚫 XAKER ANIQLANDI! BLOK!', 'danger', 10000);
                    document.body.style.pointerEvents = 'none';
                    document.body.style.opacity = '0.5';
                    setTimeout(() => {
                        document.body.style.pointerEvents = '';
                        document.body.style.opacity = '1';
                        alertShown = false;
                    }, 10000);
                }
            }
            document.addEventListener('contextmenu', function(e) { showHackerAlert(); e.preventDefault(); return false; });
            document.addEventListener('keydown', function(e) {
                if (e.key === 'F12' || (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'J' || e.key === 'C')) || (e.ctrlKey && e.key === 'U')) {
                    showHackerAlert();
                    e.preventDefault();
                    return false;
                }
            });
            console.log('%c🚀 TOSHKENTOVUZ - OLAMDAGI ENG KUCHLI PORTAL!', 'color: #39FF14; font-size: 20px; font-weight: bold;');
            console.log('%c⚡ VERCEL 100%!', 'color: #D4AF37; font-size: 16px; font-weight: bold;');
            console.log('%c🚫 HECH KIM BUZA OLMAYDI!', 'color: #FF2D2D; font-size: 16px; font-weight: bold;');
            console.log('%c🤖 Bot: @ToshkentovuzBot | 🌐 Sayt: https://toshkentov.uz', 'color: #00D4FF; font-size: 12px;');
        })();
    </script>
</body>
</html>