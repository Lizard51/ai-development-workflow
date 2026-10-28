# Установка / Installation

Пакет содержит три отдельных скилла. `grilling` нужен для основного интервью; `domain-modeling` используется только при неоднозначной предметной области или существенных архитектурных решениях. Установите все три для полного комплекта.

The package contains three separate skills. Install all three for the complete workflow; domain modeling is used only when the task needs it.

## Через Codex / With Codex

```text
$skill-installer Install from https://github.com/Lizard51/ai-development-workflow
these paths: skills/ai-development-workflow, skills/grilling,
skills/domain-modeling. If a skill already exists, preserve it and explain
the version conflict instead of overwriting it.
```

Для воспроизводимой версии попросите использовать тег `v1.0.0`. Ветка `main` может меняться. / Request tag `v1.0.0` for a fixed snapshot; `main` may change.

## Вручную / Manual installation

Скачайте исходники со [страницы релизов](https://github.com/Lizard51/ai-development-workflow/releases) либо клонируйте:

```sh
git clone --branch v1.0.0 --depth 1 https://github.com/Lizard51/ai-development-workflow.git
```

Для одного проекта скопируйте три папки из `skills/` в `.agents/skills/` внутри нужного проекта. Для пользовательской установки скопируйте их в `~/.agents/skills/`.

For one project, copy the three folders under `skills/` into that project's `.agents/skills/`. For user-wide discovery, use `~/.agents/skills/`.

```text
.agents/skills/
├── ai-development-workflow/
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/
│   └── references/
├── grilling/
│   └── SKILL.md  (+ companion files)
└── domain-modeling/
    └── SKILL.md  (+ companion files)
```

Не копируйте только `SKILL.md`: относительные ссылки требуют остальных файлов. Не заменяйте существующие скиллы без сравнения. Если используете встроенный установщик, путь выбирает он; не создавайте вторую копию того же скилла вручную.

Copy each complete skill folder, not just its entrypoint. Compare existing installations before replacing them. When using the built-in installer, keep its chosen installation location and avoid duplicate copies.

## Проверка / Check

1. Убедитесь, что все три скилла доступны в селекторе Codex; при необходимости перезапустите приложение.
2. Начните запрос с `$ai-development-workflow` и опишите задачу.
3. На существенной новой задаче агент должен сначала изучить контекст и уточнить решения. Документы и реализация следуют после подтверждения требований.

Verify skill discovery, invoke `$ai-development-workflow`, and check that a substantial new task starts with discovery and an interview before implementation.

Модели и инструменты зависят от вашей среды. Отсутствие субагентов не должно превращаться в выдуманный отчёт об их работе; скилл предусматривает явное объяснение и работу координатором.

Model and tool availability depends on the host. Missing delegation must be disclosed rather than simulated in the report.

Актуальные правила обнаружения и установки: [официальная документация OpenAI](https://learn.chatgpt.com/docs/build-skills). Установка через этот репозиторий предоставляет локальные скиллы; установка плагина в каталог ChatGPT не входит в этот проект.
