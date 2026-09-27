Custom Invoice and Job Order System

An Odoo module I built for a manufacturing business that produces items based on custom dimensions, such as height and width. It automatically generates invoices and links each one to a matching job order, so the production team always works from accurate, up to date job details.

What it does

The module extends Odoo's invoicing so that each invoice line can carry job details like height, width, unit of measure, and number of items. When an invoice is confirmed, a job order is created automatically from those lines, so sales and production always stay in sync.

Key features

Automatic job order creation from a confirmed invoice.
Real time price calculation based on dimensions, so the total updates as the user enters height, width and number of items.
Unit conversion between metres and feet, so staff can enter measurements the way they naturally think about them.
Support for multiple items on a single invoice, each with its own dimensions and pricing.
Docker based deployment, so the module can be set up quickly in a new Odoo environment.

Technical details

Built with Python and the Odoo ORM.
Custom models for job orders and job order lines, linked to Odoo's standard invoice model.
Computed fields for area and total price, using api.depends, so values stay accurate whenever the user changes an input.
An onchange method that updates the invoice quantity live as dimensions are entered.
A custom action on invoices that creates a job order directly from the invoice screen.

Setup

Add the custom_invoice_description module to your Odoo addons path.
Run the project with docker-compose.yml for a quick local setup.
