export interface Asset {
  id: string;
  filename: string;
  mime_type: string;
  thumbnail_url: string;
  width: number;
  height: number;
  tags: string[];
  dominant_colors: string[];
  created_at: string;
}

export type FilterCategory = 'all' | 'image' | 'video' | 'vector' | 'document';