# Примеры / Examples

Это примеры запросов и ожидаемого процесса, а не отчёты о выполненных проектах. / These are illustrative prompts and expected workflows, not completed-project evidence.

## Новое приложение

```text
$ai-development-workflow
Нужно локальное приложение для учёта заказов мастерской.
Один компьютер, несколько статусов заказа, данные должны переживать сбой.
Изучи папку проекта, помоги принять оставшиеся решения и реализуй
согласованный вариант с проверками восстановления данных.
```

Ожидаемый ход: обнаружение контекста → интервью → подтверждённые требования → документы в `.codex/` → тесты сохранности и восстановления → ожидаемое падение → реализация → проверка. Наличие установщика или успешный запуск нельзя заявлять без соответствующей проверки.

## Крупная функция в существующем проекте

```text
$ai-development-workflow
Добавь экспорт заказов в CSV. Сначала посмотри модель данных и текущие
тесты, уточни состав полей и правила экранирования. После согласования
реализуй экспорт и проверь пустые данные, Unicode, кавычки и переносы строк.
```

Агент должен сохранить принятые в проекте соглашения и отделить исходные сбои тестов от новых. Параллельная работа полезна только при независимых задачах и безопасной изоляции.

## Existing project, English prompt

```text
$ai-development-workflow
Add CSV export to the existing order tracker. Inspect its data model and
test suite, clarify field selection and escaping, then implement the agreed
behavior. Verify empty input, Unicode, quotes, and embedded newlines.
```

Expected: inspect first, resolve actual decisions, record the contract, verify failing acceptance tests, implement, and validate the affected flow. Preserve unrelated user changes.

## Среда без субагентов / Without delegation

```text
$ai-development-workflow
Реализуй согласованную функцию. Если среда не поддерживает субагентов
или указанные профили моделей, объясни ограничение и продолжай сам.
```

Основной агент выполняет работу последовательно, сохраняя требования, тесты и итоговую проверку. / The coordinator works sequentially while preserving the contract and verification steps.
