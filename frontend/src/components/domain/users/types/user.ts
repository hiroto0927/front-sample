export type TPropsUser = {
  id: number;
  name: string;
  is_admin: boolean;
  is_active: boolean;
  is_notice: boolean;
  created_at: string;
  updated_at: string;
};

export type TPropsUpdateUser = {
  name?: string;
  is_admin?: boolean;
  is_active?: boolean;
  is_notice?: boolean;
};
