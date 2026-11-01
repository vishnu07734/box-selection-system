# BoxWise — Django Box Selection System

A small Django application for managing products, shipping boxes and orders, then recommending the lowest-cost box that passes weight and 3D packing checks.

## Features

- Product catalogue with dimensions and weight.
- Shipping-box catalogue with internal dimensions, weight capacity and cost.
- Order creation and quantity editing through Django admin.
- Box recommendation with a reason for each rejected box.
- Six axis-aligned orientations per rectangular product.
- Deterministic, non-overlapping 3D placement heuristic.
- Automated Django tests.
- SQLite database and server-rendered HTML/CSS frontend.

## Technology

- Python 3.10+
- Django 5.x
- SQLite
- HTML, CSS and Django templates

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Create database tables
python manage.py migrate

# 4. (Optional) Create admin login
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the application and http://127.0.0.1:8000/admin/ for Django admin.

## First-use walkthrough

1. Open **Products** and add products. Dimensions use centimetres; weight uses kilograms.
2. Open **Boxes** and add boxes. Enter *internal* dimensions, maximum weight and cost.
3. Select **New order**, choose one or more products and create the order.
4. Review the recommendation and each box's eligibility explanation.
5. To change quantities, open Django admin, select the order and edit its order items. Return to the order detail page to recalculate.

The browser order form initially creates one unit of each selected product. Quantity changes are supported through the admin inline.

## Recommendation logic

For each box:

1. Sum the weights of all ordered units and reject the box if the total exceeds its maximum weight.
2. Expand quantities into individual rectangular items.
3. Sort items by descending volume.
4. For each item, try its unique axis-aligned orientations and candidate positions at the origin and at far faces of previously placed items.
5. Reject a placement if it exceeds the box dimensions or overlaps an existing placement.
6. A box is eligible only if all items are placed.
7. Select the eligible box with the lowest cost. Ties are broken by smaller internal volume and then box name.

### Important limitations and assumptions

This is a deterministic heuristic for 3D rectangular packing, not an exact solver. A failed heuristic attempt does **not** prove that no possible arrangement exists; it means this algorithm did not find one. Products are assumed to be rigid cuboids, rotation is limited to axis-aligned permutations, and padding, packaging material, fragility, orientation restrictions, and box wall thickness are not modelled. The candidate-position strategy is intentionally bounded and may miss valid layouts. For production use, consider a validated packing library or an exact/stronger optimization solver, and add business rules for handling constraints.

## Tests

```bash
python manage.py test
```

The tests cover cheapest eligible selection, weight rejection, dimension rejection, rotation, multiple-item placement, aggregated order weight, empty box catalogues and a basic web form flow.

## Repository submission checklist

- [ ] Push the project to your GitHub repository.
- [ ] Update this README if you change the algorithm or workflow.
- [ ] Complete `AI_USAGE.md` accurately, including prompts, accepted/rejected output, mistakes and verification.
- [ ] Export and attach your actual chat transcript yourself, as required by the assignment.
- [ ] Write your own learning reflection; do not use AI to generate it.
- [ ] Run the test suite and paste the real terminal output into `TEST_OUTPUT.md` or provide a GitHub Actions run link.

## Security note

This is a local assignment/demo configuration. Before deployment, set `DEBUG=False`, use a secret key from environment variables, configure `ALLOWED_HOSTS`, enable appropriate password validators, and serve static files securely.

## Optional demo data

After running migrations, create sample products and boxes:

```bash
python manage.py seed_demo
```
