# Frontend Developer Guide

## 🎯 Purpose
This guide provides comprehensive information for frontend developers working on the Agentic RAG application. It covers setup, development practices, component architecture, and integration with the backend.

## 🚀 Quick Start

### Prerequisites
- **Node.js 18+** - [Download here](https://nodejs.org/)
- **npm** or **yarn** package manager
- **Git** for version control

### Initial Setup
```bash
# Clone the repository
git clone https://github.com/your-org/agentic-rag.git
cd agentic-rag/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Environment Configuration
```bash
# Copy environment file
cp .env.example .env.local

# Configure environment variables
# - API endpoints
# - Feature flags
# - Authentication settings
```

## 🏗️ Project Structure

```
frontend/
├── src/
│   ├── app/                 # Next.js App Router pages
│   │   ├── layout.tsx       # Root layout with providers
│   │   ├── page.tsx         # Landing page
│   │   ├── chat/            # Chat interface
│   │   ├── documents/       # Document management
│   │   ├── dashboard/       # Analytics dashboard
│   │   └── admin/           # Admin panel
│   ├── components/          # Reusable UI components
│   │   ├── ui/             # Base components (Button, Input, etc.)
│   │   ├── layout/         # Layout components
│   │   ├── chat/           # Chat-specific components
│   │   └── documents/      # Document-specific components
│   ├── contexts/           # React contexts
│   │   ├── auth-context.tsx # Authentication context
│   │   └── theme-context.tsx # Theme context
│   ├── hooks/              # Custom React hooks
│   │   ├── useAuth.ts      # Authentication hook
│   │   ├── useChat.ts      # Chat functionality hook
│   │   └── useWebSocket.ts # WebSocket connection hook
│   ├── lib/                # Utility libraries
│   │   ├── api.ts          # API client
│   │   └── auth.ts         # Authentication utilities
│   └── types/              # TypeScript type definitions
├── tests/                  # Test files
│   ├── e2e/               # End-to-end tests
│   ├── fixtures/          # Test fixtures
│   └── mocks/             # Mock data and handlers
├── public/                # Static assets
└── configuration files   # Next.js, Tailwind, etc.
```

## 🔧 Development Workflow

### Running the Development Server
```bash
# Start with hot reload
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

### Testing
```bash
# Run unit tests
npm test

# Run end-to-end tests
npm run test:e2e

# Run tests with coverage
npm run test:coverage
```

### Code Quality
```bash
# Format code
npm run format

# Lint code
npm run lint

# Type checking
npm run type-check
```

## 🎨 UI Components

### Component Architecture
- **Functional Components** with hooks
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **React Query** for data fetching

### Creating New Components
1. Create component in appropriate directory under `src/components/`
2. Add TypeScript interfaces for props
3. Include Storybook stories (if applicable)
4. Write unit tests
5. Document component usage

### Styling Guidelines
- Use Tailwind CSS utility classes
- Follow design system tokens
- Responsive design with mobile-first approach
- Dark mode support with theme context

## 🔌 API Integration

### API Client
The `src/lib/api.ts` file provides a configured Axios instance:
```typescript
import { api } from '@/lib/api'

// Example API call
const response = await api.get('/api/v1/documents')
```

### Authentication
JWT authentication is handled automatically:
- Tokens stored in HTTP-only cookies
- Automatic token refresh
- Protected route components

### Real-time Updates
WebSocket integration for chat functionality:
```typescript
const { messages, sendMessage } = useWebSocket()
```

## 📱 Key Features Implementation

### Chat Interface
- Real-time message streaming
- Message history persistence
- File attachment support
- Typing indicators

### Document Management
- Drag-and-drop file upload
- Processing status tracking
- Document search and filtering
- Bulk operations

### Authentication Flow
- JWT-based authentication
- Role-based access control
- Protected routes
- Session management

## 🧪 Testing Strategy

### Unit Tests
- Component rendering and interaction
- Hook functionality
- Utility functions

### Integration Tests
- Component composition
- API integration
- State management

### E2E Tests
- User workflows
- Cross-browser testing
- Accessibility testing

### Test Utilities
- Mock API responses
- Test data factories
- Custom render functions

## 🚀 Performance Optimization

### Code Splitting
- Dynamic imports for routes
- Lazy loading of components
- Bundle analysis

### Caching Strategy
- React Query for server state
- Local storage for user preferences
- CDN for static assets

### Image Optimization
- Next.js Image component
- Responsive images
- WebP format support

## 🔒 Security Considerations

### Input Validation
- Client-side form validation
- XSS prevention
- CSRF protection

### Data Protection
- Secure cookie handling
- Encryption of sensitive data
- Privacy-focused analytics

### Content Security
- CSP headers configuration
- Sanitization of user content
- Secure file upload handling

## 📦 Deployment

### Build Process
```bash
# Create production build
npm run build

# Analyze bundle size
npm run analyze
```

### Environment Variables
Required environment variables for production:
```env
NEXT_PUBLIC_API_URL=https://api.your-domain.com
NEXT_PUBLIC_WS_URL=wss://api.your-domain.com
NEXTAUTH_URL=https://your-domain.com
NEXTAUTH_SECRET=your-secret-key
```

### Docker Deployment
```dockerfile
# Use the provided Dockerfile
docker build -t frontend-app .
```

## 🐛 Troubleshooting

### Common Issues
- **CORS errors**: Check API URL configuration
- **Authentication issues**: Verify token storage and refresh
- **Build failures**: Check Node.js version compatibility
- **Styling issues**: Verify Tailwind CSS purge configuration

### Debugging
```bash
# Enable debug logging
DEBUG=true npm run dev

# Use React DevTools browser extension
# Use browser developer tools
```

### Getting Help
- Check the [Troubleshooting Guide](../TROUBLESHOOTING.md)
- Review existing GitHub issues
- Ask in the team Slack channel

## 📚 Learning Resources

### Next.js
- [Official Documentation](https://nextjs.org/docs)
- [Learn Next.js](https://nextjs.org/learn)

### React
- [React Documentation](https://react.dev/)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)

### Tailwind CSS
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Tailwind UI Components](https://tailwindui.com/)

### Testing
- [Jest Documentation](https://jestjs.io/)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)

## 🔄 Contributing

### Code Standards
- Follow TypeScript strict mode
- Use functional components and hooks
- Write comprehensive tests
- Document complex logic

### Pull Request Process
1. Create feature branch from `develop`
2. Implement changes with tests
3. Run all tests and ensure they pass
4. Update documentation if needed
5. Submit PR for review

### Review Guidelines
- Check for accessibility compliance
- Verify responsive design
- Test cross-browser compatibility
- Ensure performance optimization

---

*This guide is maintained by the frontend development team. Please contribute improvements and updates as needed.*