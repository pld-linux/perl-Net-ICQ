%define	pdir	Net
%define	pnam	ICQ
%include	/usr/lib/rpm/macros.perl
Summary:	Net-ICQ perl module
Summary(pl):	Modu� perla Net-ICQ
Name:		perl-Net-ICQ
Version:	0.16
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Text-LineEditor
Requires:	perl-Text-LineEditor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-ICQ - simple ICQ client in Perl.

%description -l pl
Net-ICQ - prosty klient ICQ.

%prep
%setup -q -n Net-ICQ-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz test*.pl
%{perl_sitelib}/Net/ICQ.pm
%{_mandir}/man3/*
