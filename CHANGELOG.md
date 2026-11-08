# Changelog

All notable changes to AIMS-mini will be documented in this file.

## [Unreleased]

## [1.0.0] - 2026-11-08

### Added
- Add `Cart.print_cart()` to display cart items.
- Add `Cart.search_by_title()` to search DVDs.
- Add `Cart.discounted_total()` to calculate discounted totals.
- Add unit tests for cart limits and discounts.
- Add Pull Request template and use case documentation.

### Fixed
- Fix cart capacity limit to reject the 21st DVD.
- Fix discount calculation and validate discount percentage.
- Handle empty cart when displaying items.

### Changed
- Reorganize source code into the `aims` Python package.
