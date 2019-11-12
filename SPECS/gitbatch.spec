%define debug_package %{nil}

%global gh_user  isacikgoz

Name:           gitbatch
Version:        0.5.0
Release:        1%{?dist}
Summary:        Manage your git repositories in one place
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  git golang

%description
Managing multiple git repositories is easier than ever. I (was) often end up working on
many directories and manually pulling updates etc. To make this routine faster, I created
a simple tool to handle this job. Although the focus is batch jobs, you can still do de
facto micro management of your git repositories (e.g add/reset, stash, commit etc.)

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar -xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
ln -snf %{_builddir}/%{name}-%{version} %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
export GO111MODULE=on
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Nov 11 2019 Jamie Curnow <jc@jc21.com> 0.5.0-1
- Initial Spec
