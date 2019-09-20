import { CoreUIPage } from './app.po';

describe('K-Portal App', function() {
  let page: CoreUIPage;

  beforeEach(() => {
    page = new CoreUIPage();
  });

  it('should display footer containing creativeLabs', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toContain('creativeLabs');
  });
});
