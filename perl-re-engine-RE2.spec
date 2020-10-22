#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	re
%define	pnam	engine-RE2
Summary:	re::engine::RE2 - RE2 regex engine
Name:		perl-re-engine-RE2
Version:	0.13
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DG/DGL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	85bf2cf9be48d287fdd3b0037cd9cefd
URL:		http://search.cpan.org/dist/re-engine-RE2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module replaces perl's regex engine in a given lexical scope with
RE2. RE2 is a primarily DFA based regexp engine from Google that is
very fast at matching large amounts of text. However it does not
support look behind and some other Perl regular expression features.
See RE2's website for more information. Fallback to normal Perl regexp
is implemented by this module. If RE2 is unable to compile a regexp it
will use Perl instead, therefore features not implemented by RE2 don't
suddenly stop working, they will just use Perl's regexp implementation.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/re/engine/RE2.pm
%dir %{perl_vendorarch}/auto/re/engine/RE2
%attr(755,root,root) %{perl_vendorarch}/auto/re/engine/RE2/RE2.so
%{_mandir}/man3/re::engine::RE2.3pm*
