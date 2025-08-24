# Enterprise RAG Chatbot - UI Tests

Comprehensive Playwright testing framework for the Enterprise RAG Chatbot UI. This test suite provides end-to-end testing coverage for all user interfaces and workflows.

## 🎯 Overview

This testing framework uses Playwright to provide:
- **Cross-browser testing** (Chrome, Firefox, Safari)
- **Mobile and responsive testing**
- **API integration testing through UI**
- **Authentication and authorization testing**
- **Performance and accessibility testing**
- **End-to-end workflow testing**

## 📁 Structure

```
tests/ui/
├── fixtures/           # Test fixtures and utilities
│   └── test-fixtures.ts
├── pages/              # Page Object Model classes
│   ├── base-page.ts
│   ├── login-page.ts
│   ├── chat-page.ts
│   ├── documents-page.ts
│   ├── dashboard-page.ts
│   └── admin-page.ts
├── specs/              # Test specifications
│   ├── auth.spec.ts
│   ├── chat.spec.ts
│   ├── documents.spec.ts
│   ├── dashboard.spec.ts
│   ├── admin.spec.ts
│   └── e2e-workflow.spec.ts
├── utils/              # Test utilities and helpers
│   ├── auth-service.ts
│   ├── test-data-service.ts
│   ├── test-helpers.ts
│   ├── global-setup.ts
│   └── global-teardown.ts
├── data/               # Test data and environment config
│   └── test-env.ts
├── playwright.config.ts # Playwright configuration
├── package.json
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ installed
- Docker and Docker Compose
- Backend services running

### Installation

1. **Install dependencies:**
```bash
cd tests/ui
npm install
npm run setup  # Installs Playwright browsers
```

2. **Environment setup:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Start backend services:**
```bash
npm run docker:up
```

### Running Tests

#### Basic Commands

```bash
# Run all tests
npm test

# Run with browser visible
npm run test:headed

# Run in debug mode
npm run test:debug

# Run with UI mode
npm run test:ui
```

#### Specific Test Suites

```bash
# Authentication tests
npm run test:auth

# Chat functionality tests
npm run test:chat

# Document management tests
npm run test:documents

# Dashboard tests
npm run test:dashboard

# Admin panel tests
npm run test:admin

# End-to-end workflow tests
npm run test:e2e
```

#### Device-Specific Tests

```bash
# Mobile tests
npm run test:mobile

# Desktop browsers
npm run test:desktop

# Specific browser
npx playwright test --project=chromium
```

#### Test Categories

```bash
# Smoke tests (quick validation)
npm run test:smoke

# Regression tests (comprehensive)
npm run test:regression

# Parallel execution
npm run test:parallel
```

## 🧪 Test Categories

### 1. Authentication Tests (`auth.spec.ts`)
- Login/logout flows
- Session management
- Role-based access control
- Security validations
- Password recovery

### 2. Chat Tests (`chat.spec.ts`)
- Message sending/receiving
- RAG integration
- WebSocket functionality
- Conversation management
- Streaming responses
- Error handling

### 3. Document Tests (`documents.spec.ts`)
- File upload (single/multiple)
- Document listing/searching
- Bulk operations
- Processing status
- File type validation
- Drag & drop functionality

### 4. Dashboard Tests (`dashboard.spec.ts`)
- Statistics display
- Recent activity
- Quick actions
- System status
- Navigation
- Responsive design

### 5. Admin Tests (`admin.spec.ts`)
- User management
- System settings
- Analytics
- Audit logs
- Permissions
- Configuration

### 6. E2E Workflow Tests (`e2e-workflow.spec.ts`)
- Complete user journeys
- Multi-user scenarios
- Error recovery
- Performance under load
- Data consistency

## 📋 Page Object Model

### Base Page (`base-page.ts`)
Common functionality shared across all pages:
- Navigation helpers
- Loading state management
- Error handling
- Screenshot utilities
- Accessibility helpers

### Specialized Pages
Each page class provides:
- Element selectors
- Page-specific actions
- Validation methods
- Helper utilities

Example usage:
```typescript
test('should upload document', async ({ documentsPage }) => {
  await documentsPage.goto();
  await documentsPage.performDocumentUpload('test.txt', 'content');
});
```

## 🔧 Configuration

### Playwright Config (`playwright.config.ts`)
- Multi-browser setup
- Device emulation
- Test timeouts
- Reporter configuration
- WebServer integration

### Environment Variables (`.env`)
Key configurations:
```env
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
HEADLESS=true
WORKERS=2
DEBUG_MODE=false
```

## 🛠️ Utilities and Services

### Auth Service (`auth-service.ts`)
- User authentication
- Token management
- Role-based testing
- Session handling

### Test Data Service (`test-data-service.ts`)
- Test document creation
- Conversation setup
- Data cleanup
- Fixture management

### Test Helpers (`test-helpers.ts`)
- Common UI interactions
- Wait utilities
- Screenshot helpers
- API mocking
- WebSocket testing

## 📊 Test Reports

### Available Reporters
- **HTML Report**: `npx playwright show-report`
- **JUnit XML**: For CI integration
- **JSON Report**: Programmatic access
- **Trace Viewer**: `npx playwright show-trace`

### CI Integration
```yaml
# GitHub Actions example
- name: Run Playwright tests
  run: |
    cd tests/ui
    npm ci
    npm run test:ci
    
- name: Upload test results
  uses: actions/upload-artifact@v3
  with:
    name: playwright-report
    path: tests/ui/playwright-report/
```

## 🎭 Test Patterns

### Fixtures Usage
```typescript
test('should handle authenticated user', async ({ 
  authenticatedPage, 
  chatPage 
}) => {
  // User already logged in via fixture
  await chatPage.performChatInteraction('Hello!');
});
```

### Data Generation
```typescript
import { testData } from '../fixtures/test-fixtures';

const user = testData.generateUser();
const document = testData.generateDocument();
```

### Error Testing
```typescript
test('should handle API errors', async ({ chatPage, testHelpers }) => {
  await testHelpers.mockApiResponse(/\/api\/v1\/chat/, {
    error: 'Service unavailable'
  }, 500);
  
  await chatPage.sendMessage('Test message');
  await chatPage.verifyToast('Service unavailable', 'error');
});
```

## 🔍 Debugging

### Debug Mode
```bash
# Step through tests
npm run test:debug

# Specific test
npx playwright test auth.spec.ts --debug
```

### Trace Viewer
```bash
# Generate traces
npx playwright test --trace on

# View traces
npx playwright show-trace trace.zip
```

### Screenshots
Tests automatically capture screenshots on failure. Manual screenshots:
```typescript
await page.screenshot({ path: 'debug.png' });
```

## 📱 Mobile Testing

### Device Configuration
Tests run on multiple device types:
- iPhone 12
- Pixel 5
- iPad
- Desktop viewports

### Responsive Testing
```typescript
test('should work on mobile', async ({ chatPage }) => {
  await chatPage.verifyResponsiveLayout('mobile');
  await chatPage.performChatInteraction('Mobile test');
});
```

## ♿ Accessibility Testing

### Built-in Checks
- ARIA labels
- Keyboard navigation
- Color contrast
- Screen reader compatibility

### Manual Testing
```typescript
test('should be accessible', async ({ chatPage }) => {
  await chatPage.verifyAccessibility();
});
```

## 🚀 Performance Testing

### Performance Monitoring
```typescript
test('should load quickly', async ({ dashboardPage }) => {
  const startTime = Date.now();
  await dashboardPage.goto();
  const loadTime = Date.now() - startTime;
  expect(loadTime).toBeLessThan(5000);
});
```

### Load Testing
```bash
# Concurrent user simulation
WORKERS=10 npm test
```

## 🔒 Security Testing

### XSS Prevention
```typescript
test('should prevent XSS', async ({ loginPage }) => {
  await loginPage.login('<script>alert("xss")</script>', 'password');
  // Should not execute script
});
```

### CSRF Protection
```typescript
test('should handle CSRF tokens', async ({ chatPage }) => {
  // Tests include CSRF token validation
});
```

## 📦 Docker Integration

### Running with Docker
```bash
# Start services
npm run docker:up

# Run tests
npm test

# Cleanup
npm run docker:down
```

### CI/CD Pipeline
```dockerfile
FROM mcr.microsoft.com/playwright:v1.40.1-focal

WORKDIR /app
COPY tests/ui/package*.json ./
RUN npm ci

COPY tests/ui/ ./
CMD ["npm", "test"]
```

## 🐛 Troubleshooting

### Common Issues

1. **Tests timing out**
   - Increase timeout in config
   - Check service availability
   - Verify network connectivity

2. **Authentication failures**
   - Verify test user credentials
   - Check backend authentication
   - Clear browser state

3. **File upload issues**
   - Check file permissions
   - Verify upload directory
   - Test file size limits

4. **WebSocket failures**
   - Check WebSocket endpoint
   - Verify connection handling
   - Test network stability

### Debug Commands
```bash
# Verbose output
npx playwright test --reporter=line

# Specific test with trace
npx playwright test login --trace on

# Test with specific browser
npx playwright test --project=firefox
```

## 📈 Metrics and Monitoring

### Test Metrics
- Test execution time
- Pass/fail rates
- Coverage metrics
- Performance benchmarks

### Monitoring Integration
- Prometheus metrics
- Grafana dashboards
- Alert configurations
- Performance tracking

## 🤝 Contributing

### Adding New Tests
1. Create test spec in `specs/`
2. Add page objects in `pages/`
3. Update fixtures if needed
4. Document test scenarios

### Test Guidelines
- Use descriptive test names
- Follow Page Object Model
- Include error scenarios
- Test responsive design
- Verify accessibility

### Code Style
```bash
# Lint tests
npm run lint

# Type checking
npm run type-check
```

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/)
- [Page Object Model Guide](https://playwright.dev/docs/pom)
- [Best Practices](https://playwright.dev/docs/best-practices)
- [CI/CD Integration](https://playwright.dev/docs/ci)

## 📞 Support

For issues or questions:
1. Check existing test documentation
2. Review error logs and traces
3. Create issue with reproduction steps
4. Include environment details

---

**Note**: This testing framework is designed to work with the Enterprise RAG Chatbot backend. Ensure all services are running before executing tests.