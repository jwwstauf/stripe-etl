create_subscription_schema = """CREATE SCHEMA IF NOT EXISTS subscriptions;"""

create_subscription_table = """
CREATE TABLE IF NOT EXISTS subscriptions (
	subscription_id varchar PRIMARY KEY,
	billing_cycle_anchor date,
	cancel_at date,
	cancel_at_period_end boolean, 
	canceled_at date,
	created date,
	current_period_end date,
	current_period_start date,
	customer_id varchar,
	ended_at date,
	quantity smallint,
    start_date date,
    status varchar
    );
"""

insert__table = """
INSERT INTO postgres.subscriptions VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (subscription_id)
    DO UPDATE SET
    subscription_id = EXCLUDED.subscription_id,
    billing_cycle_anchor = EXCLUDED.billing_cycle_anchor,
    cancel_at = EXCLUDED.cancel_at,
    cancel_at_period_end = EXCLUDED.cancel_at_period_end,
    canceled_at = EXCLUDED.canceled_at,
    created = EXCLUDED.created,
    current_period_end = EXCLUDED.current_period_end,
    current_period_start = EXCLUDED.current_period_start,
    customer_id = EXCLUDED.customer_id,
    ended_at = EXCLUDED.ended_at,
    quantity = EXCLUDED.quantity,
    start_date = EXCLUDED.start_date,
    status = EXCLUDED.status;
"""