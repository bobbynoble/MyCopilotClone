---
name: powerapps-standards
description: Coding standards, naming conventions and performance patterns for Power Apps canvas and model-driven apps (Power Fx). Use when writing, generating or reviewing any Power Apps formula, screen, control or app structure.
---

# Power Apps Standards

## Naming conventions

### Screens
Plain-English name ending in `Screen`: `Home Screen`, `Request Details Screen`.

### Controls — `prefix_ScreenAbbrev_Purpose`
| Control | Prefix | Example |
|---|---|---|
| Button | `btn` | `btn_Home_Submit` |
| Label / Text | `lbl` | `lbl_Home_Title` |
| Text input | `txt` | `txt_Req_Title` |
| Dropdown | `drp` | `drp_Req_Category` |
| Combo box | `cmb` | `cmb_Req_Approver` |
| Date picker | `dte` | `dte_Req_DueDate` |
| Toggle | `tgl` | `tgl_Req_Urgent` |
| Checkbox | `chk` | `chk_Req_Agree` |
| Gallery | `gal` | `gal_Home_Requests` |
| Form | `frm` | `frm_Req_Details` |
| Container | `con` | `con_Home_Header` |
| Icon | `ico` | `ico_Home_Back` |
| Image | `img` | `img_Home_Logo` |
| Rectangle / shape | `rec` | `rec_Home_Divider` |
| Timer | `tmr` | `tmr_Home_Refresh` |
| Component | `cmp` | `cmp_Header` |

### Variables and collections
| Type | Prefix | Example |
|---|---|---|
| Global variable (`Set`) | `gbl` | `gblCurrentUser` |
| Context variable (`UpdateContext`) | `loc` | `locShowPopup` |
| Collection | `col` | `colRequests` |
| Named formula (App.Formulas) | `nf` or plain PascalCase | `nfUserEmail` / `UserEmail` |
| `With()` scoped record | `_` prefix | `_selected` |

## Structure

- Use **containers** (horizontal/vertical) for responsive layout; avoid absolute X/Y.
- Put constants and derived values in **App.Formulas** (named formulas) rather than `App.OnStart`.
- Keep `App.OnStart` minimal; enable "Delayed load" and avoid blocking start-up.
- Build reusable headers/menus as **components** (or component library).
- Use **modern controls** and a theme rather than hand-set colours on every control.

## Power Fx patterns

- Use `With()` to name intermediate values instead of repeating lookups.
- Use `Concurrent()` to load independent data sources in parallel.
- Prefer `Patch()` with explicit records for complex saves; use `SubmitForm()` for simple forms.
- Use `IfError()` / `Errors()` around writes and `Notify()` the user on failure.
- Use `Coalesce()` / `IsBlank()` defensively on optional values.
- Comment non-obvious formulas with `//` explaining *why*.
- Format formulas with the built-in formatter before handing over.

## Delegation & performance (always check)

- Know which functions delegate for the data source (Dataverse > SharePoint > Excel).
- `Search()`, `in`, `Len()`, `CountRows()` on large SharePoint lists → non-delegable risk.
- Never rely on raising the data row limit (500 → 2000) as a "fix".
- Filter on indexed columns; for SharePoint, index columns used in filters.
- Use `ShowColumns()` to limit columns retrieved where useful.
- Avoid `LookUp()` per gallery row against remote sources; pre-join or use Dataverse relationships.
- Flag every delegation warning in the build notes with the mitigation.

## Accessibility

- Every interactive control has `AccessibleLabel`.
- Sensible `TabIndex` order; colour contrast meets WCAG AA.

## Model-driven apps

- Design the Dataverse model first (tables, relationships, choices, business rules).
- Use views/forms per role; security roles + business units, not app-level hiding.
