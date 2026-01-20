import { Asset } from "@/types/asset";

export const MOCK_ASSETS: Asset[] = [
  {
    id: "1",
    filename: "abstract-gradient-01.png",
    mime_type: "image/png",
    thumbnail_url: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=400&auto=format&fit=crop",
    width: 1920,
    height: 1080,
    tags: ["gradient", "mesh", "modern", "blue"],
    dominant_colors: ["#3b82f6", "#8b5cf6"],
    created_at: "2023-10-24T10:00:00Z"
  },
  {
    id: "2",
    filename: "minimal-interior.jpg",
    mime_type: "image/jpeg",
    thumbnail_url: "https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?q=80&w=400&auto=format&fit=crop",
    width: 3000,
    height: 2000,
    tags: ["interior", "furniture", "minimalist", "lamp"],
    dominant_colors: ["#f3f4f6", "#1f2937"],
    created_at: "2023-10-25T14:20:00Z"
  },
  {
    id: "3",
    filename: "brand-guidelines-v2.pdf",
    mime_type: "application/pdf",
    thumbnail_url: "https://images.unsplash.com/photo-1586717791821-3f44a563eb4c?q=80&w=400&auto=format&fit=crop",
    width: 800,
    height: 1100,
    tags: ["branding", "pdf", "typography"],
    dominant_colors: ["#000000", "#ffffff"],
    created_at: "2023-10-26T09:15:00Z"
  },
  {
    id: "4",
    filename: "nature-texture.heic",
    mime_type: "image/heic",
    thumbnail_url: "https://images.unsplash.com/photo-1501854140801-50d01698950b?q=80&w=400&auto=format&fit=crop",
    width: 4032,
    height: 3024,
    tags: ["nature", "green", "texture", "organic"],
    dominant_colors: ["#14532d", "#365314"],
    created_at: "2023-10-27T16:45:00Z"
  }
];