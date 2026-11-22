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

Агент должен сохранить принятые в проекте соглашения, обновить существующие требования и очередь вместо создания параллельных документов и отделить исходные сбои тестов от новых. Параллельная работа полезна только при независимых задачах и безопасной изоляции.

## Existing project, English prompt

```text
$ai-development-workflow
Add CSV export to the existing order tracker. Inspect its data model and
test suite, clarify field selection and escaping, then implement the agreed
behavior. Verify empty input, Unicode, quotes, and embedded newlines.
```

Expected: inspect first, resolve actual decisions, record the contract, verify failing acceptance tests, implement, and validate the affected flow. Preserve unrelated user changes.

## Проверка результата и замены / Checking outcomes and replacements

Если CSV предназначен для конкретной программы, проверка должна дойти до открытия файла в ней, а не только подтвердить создание файла. При замене старого экспорта проверьте затронутые вызовы, тесты, ссылки и инструкции; изменённую документированную команду выполните в указанном виде или объясните препятствие. Сохраняйте исторические материалы с пометкой об их статусе. Добавляйте проверку отказа или конфликта, если возможна потеря данных или блокировка работы; для небольшой правки достаточно узкой проверки её поведения.

If the CSV is intended for a particular application, verify that it opens there, not merely that a file was created. When replacing the old export, reconcile affected callers, tests, links, and instructions; run a changed documented command exactly as shown or explain what prevented it. Retain historical material with its status clearly marked. Check a failure or conflict when data loss or blocked work is possible; a small edit needs only a focused check of its behavior.

## Как выбирается исполнитель / How the coordinator picks a worker

В примере с CSV координатор может поручить Luna Medium найти текущие тесты, а Terra Medium — реализовать согласованные правила экспорта. Если экспорт требует согласованного снимка данных во время параллельных изменений, Sol Medium можно сразу поручить проектирование проверок и реализацию этой части. Если обычный экспорт не проходит тест, координатор сначала сверяет ожидаемый результат с требованиями и решает, достаточно ли локальной доработки.

For the CSV example, Luna Medium can locate the existing tests and Terra Medium can implement the agreed export behavior. If the export must read a consistent snapshot while data changes concurrently, the coordinator can assign the test design and implementation for that part directly to Sol Medium. If a routine export test fails, the coordinator checks the expected result against the requirements before deciding whether a local correction is enough.

## Среда без субагентов / Without delegation

```text
$ai-development-workflow
Реализуй согласованную функцию. Если среда не поддерживает субагентов
или указанные профили моделей, объясни ограничение и продолжай сам.
```

Основной агент выполняет работу последовательно, сохраняя требования, тесты и итоговую проверку. / The coordinator works sequentially while preserving the contract and verification steps.
