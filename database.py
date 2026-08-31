from supabase import create_client

SUPABASE_URL = "https://xeeoryivwbmrzmjnawue.supabase.co"

SUPABASE_KEY = "sb_publishable_-m6BDKqy82uyMAXqS129Eg_vrgbQA5S"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)