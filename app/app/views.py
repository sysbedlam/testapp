from django.http import HttpResponse

def index(request):
    return HttpResponse("""
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Дипломная работа — Балашов Егор</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #0d1117; color: #e6edf3; min-height: 100vh; display: flex; flex-direction: column; }
    header { padding: 24px 40px; border-bottom: 1px solid #21262d; display: flex; justify-content: space-between; align-items: center; }
    header .logo { color: #19865C; font-size: 1.1em; font-weight: 600; }
    header .school { color: #8b949e; font-size: 0.9em; }
    main { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px 20px; text-align: center; }
    .rocket { font-size: 72px; margin-bottom: 24px; animation: float 3s ease-in-out infinite; }
    @keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-12px); } }
    h1 { font-size: 2.4em; font-weight: 600; margin-bottom: 8px; }
    h1 span { color: #19865C; }
    .subtitle { color: #8b949e; font-size: 1.1em; margin-bottom: 48px; }
    .stack { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-bottom: 48px; }
    .badge { background: #161b22; border: 1px solid #21262d; color: #e6edf3; padding: 8px 18px; border-radius: 6px; font-size: 0.9em; transition: border-color .2s; }
    .badge:hover { border-color: #19865C; color: #19865C; }
    .info { background: #161b22; border: 1px solid #21262d; border-radius: 10px; padding: 24px 40px; display: inline-block; }
    .info p { color: #8b949e; font-size: 0.85em; margin-bottom: 6px; }
    .info h2 { font-size: 1.2em; font-weight: 500; }
    footer { padding: 20px; text-align: center; color: #8b949e; font-size: 0.85em; border-top: 1px solid #21262d; }
  </style>
</head>
<body>
  <header>
    <span class="logo">django + kubernetes</span>
    <span class="school">SkillFactory DevOps 2026</span>
  </header>
  <main>
    <div class="rocket">🚀</div>
    <h1>Дипломная работа <span>Балашова Егора</span></h1>
    <p class="subtitle">Полный цикл CI/CD — от кода до продакшена</p>
    <div class="stack">
      <span class="badge">Terraform</span>
      <span class="badge">Ansible</span>
      <span class="badge">Kubernetes</span>
      <span class="badge">Helm</span>
      <span class="badge">GitHub Actions</span>
      <span class="badge">Docker</span>
      <span class="badge">Prometheus</span>
      <span class="badge">Grafana</span>
      <span class="badge">Loki</span>
      <span class="badge">Yandex Cloud</span>
    </div>
    <div class="info">
      <p>Студент</p>
      <h2>Балашов Егор Дмитриевич</h2>
    </div>
  </main>
  <footer>SkillFactory · DevOps Diploma · 2026</footer>
</body>
</html>
""")
