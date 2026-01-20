-- Enforce Row-Level Security (RLS) to prevent cross-tenant data leaks
-- This ensures a freelancer can only query THEIR own assets even if the app has a bug.

ALTER TABLE assets ENABLE ROW LEVEL SECURITY;

-- Policy: Users can only see assets they own
CREATE POLICY asset_isolation_policy ON assets
    USING (owner_id = current_setting('app.current_user_id')::uuid);

-- Policy: Only owners can delete their IP
CREATE POLICY asset_delete_policy ON assets
    FOR DELETE
    USING (owner_id = current_setting('app.current_user_id')::uuid);

-- Audit Log Table: Track every time an asset is accessed/downloaded
CREATE TABLE security_audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    asset_id UUID NOT NULL,
    action TEXT NOT NULL, -- 'VIEW', 'DOWNLOAD', 'GENERATE_URL'
    ip_address TEXT,
    user_agent TEXT,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);